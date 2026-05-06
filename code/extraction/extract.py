import argparse, datetime as dt, hashlib, json, os, re, subprocess, urllib.request
from .scoring import compute_confidence

UA = "Stephen Wang (Abel AI Lab) lab@abel.ai"; LOGDIR = "abelian/runs/2026-05-05-path-c-1week-probe/round-2/prompt_logs"
KEYS = "deal_type ticker_target ticker_acquirer consideration_per_share_cash_or_null consideration_per_share_stock_ratio_or_null expected_close_date tender_deadline_or_null proration_threshold_pct_or_null regulatory_agency_named_or_none_explicit financing_source_named_or_none_explicit current_target_price_or_null".split()
DEAL_RE = re.compile(r"consideration|purchase price|merger consideration|tender offer|regulatory|antitrust", re.I)

def _blank(filing, status, reason=None, chunks=0):
    out = {**filing, **{k: None for k in KEYS}, "parse_status": status, "skip_reason_or_null": reason, "prompt_log_ref": None, "response_log_ref": None, "chunks_used": chunks}
    out["confidence_extraction_pct"] = compute_confidence(out); out["annualized_spread_bps"] = None; return out

def _read(url):
    data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30).read()
    return None if url.lower().endswith(".pdf") or data.startswith(b"%PDF") else data.decode("utf-8", "ignore")

def _chunks(text):
    if len(text) <= 50000: return [text]
    m = DEAL_RE.search(text[50000:]); base = 50000
    if not m: m = DEAL_RE.search(text); base = 0
    if not m: return [text[:50000]]
    pos = base + m.start()
    return [text[:50000], text[max(0, pos - 10000):pos + 10000]]

def _spread(row):
    try:
        cash = float(row["consideration_per_share_cash_or_null"]); price = float(row["current_target_price_or_null"])
        days = (dt.date.fromisoformat(row["expected_close_date"]) - dt.date.fromisoformat(row["filed_date"])).days
        return round(((cash / price) - 1) * 365 / days * 10000, 2) if cash > 0 and price > 0 and days > 0 else None
    except Exception: return None

def _base(filing):
    url = filing.get("primary_doc_url", ""); cik = filing.get("cik") or (re.search(r"/data/(\d+)/", url) or ["", "unknowncik"])[1]
    acc = filing.get("accession_no", "unknown").replace("/", "_"); form_hash = hashlib.sha1(url.encode()).hexdigest()[:8]
    os.makedirs(LOGDIR, exist_ok=True); return f"{LOGDIR}/{acc}-{cik}-{form_hash}"

def _prompt(filing, text):
    return f"""You are reading SEC filing {filing.get('form_type')} for {filing.get('filer')} as-of filing date {filing.get('filed_date')}. Extract structured trade-checklist as JSON. Output ONLY the JSON. Required keys: {{deal_type in {{merger, tender, liquidation, rights, spin}}, ticker_target, ticker_acquirer (or null), consideration_per_share_cash_or_null, consideration_per_share_stock_ratio_or_null, expected_close_date (ISO), tender_deadline_or_null, proration_threshold_pct_or_null, regulatory_agency_named_or_none_explicit, financing_source_named_or_none_explicit, current_target_price_or_null}}.
CRITICAL DISAMBIGUATION:
- regulatory_agency_named_or_none_explicit: ONLY name HSR, FTC, DOJ, CFIUS, EU Commission, China SAMR, or other deal-clearance agency. SEC (which receives the filing) is NOT a regulatory clearance agency. If filing has no deal-clearance language -> null. If filing explicitly says "no regulatory approvals required" -> "none required".
- financing_source_named_or_none_explicit: ONLY name actual financing source (debt commitment $X / equity / bridge loan). If filing has no financing language -> null. If filing says "not subject to financing condition" -> "none required".
- this is read AS-OF filing date {filing.get('filed_date')}; do NOT use post-filing data or outside market prices.
Mark fields null when filing does not contain the information; DO NOT invent.

FILING_TEXT:
{text}"""

def _ask(prompt, prompt_path, response_path):
    open(prompt_path, "w").write(prompt)
    try:
        run = subprocess.run(["codex", "exec", "--dangerously-bypass-approvals-and-sandbox", "-c", 'model_reasoning_effort="xhigh"'], input=prompt, text=True, capture_output=True, timeout=120)
        response = (run.stdout or "").strip(); status = None
    except subprocess.TimeoutExpired:
        response = ""; status = "llm_timeout"
    open(response_path, "w").write(response); return response, status

def _finish(filing, response, status, prompt_path, response_path, chunks_used):
    out = {**filing, **{k: None for k in KEYS}, "skip_reason_or_null": None, "chunks_used": chunks_used, "prompt_log_ref": prompt_path, "response_log_ref": response_path}
    if not response:
        out["parse_status"] = status or "json_validation_failed"
    else:
        try:
            data = json.loads(response); ok = isinstance(data, dict) and all(k in data for k in KEYS); out.update(data if isinstance(data, dict) else {}); out["parse_status"] = "ok" if ok else "json_validation_failed"
        except Exception: out["parse_status"] = "llm_parse_error"
    out["confidence_extraction_pct"] = compute_confidence(out); out["annualized_spread_bps"] = _spread(out)
    if out["parse_status"] == "ok" and out["confidence_extraction_pct"] < 80: out["skip_reason_or_null"] = "confidence_below_80"
    return out

def extract_situation(filing: dict) -> dict:
    try: text = _read(filing["primary_doc_url"])
    except Exception: return _blank(filing, "json_validation_failed", "read_failed")
    if text is None: return _blank(filing, "scanned_pdf_skip", "pdf_or_scanned")
    base = _base(filing); chunks = _chunks(text)
    if len(chunks) == 1:
        prompt_path = f"{base}-prompt.txt"; response_path = f"{base}-response.txt"; response, status = _ask(_prompt(filing, chunks[0]), prompt_path, response_path)
    else:
        first, _ = _ask(_prompt(filing, chunks[0]), f"{base}-first-prompt.txt", f"{base}-first-response.txt")
        prompt_path = f"{base}-prompt.txt"; response_path = f"{base}-response.txt"
        response, status = _ask(_prompt(filing, "FIRST_SLICE_EXTRACTION_JSON:\n" + first + "\n\nDEAL_SECTION_SNIPPET:\n" + chunks[1]), prompt_path, response_path)
    return _finish(filing, response, status, prompt_path, response_path, len(chunks))

def _selected(rows, per_type_quota, max_total):
    seen = {}; picked = set()
    for i, row in enumerate(rows):
        form = row.get("form_type") or ""
        if seen.get(form, 0) < per_type_quota and len(picked) < max_total:
            picked.add(i); seen[form] = seen.get(form, 0) + 1
    return picked

def main():
    p = argparse.ArgumentParser(); p.add_argument("--filings", required=True); p.add_argument("--output", required=True)
    p.add_argument("--per-type-quota", type=int, default=4); p.add_argument("--max-total", type=int, default=20); p.add_argument("--max-files", type=int)
    a = p.parse_args(); os.makedirs(os.path.dirname(a.output), exist_ok=True)
    rows = [json.loads(line) for line in open(a.filings) if line.strip()]; picked = _selected(rows, a.per_type_quota, a.max_files or a.max_total)
    with open(a.output, "w") as out:
        for i, filing in enumerate(rows):
            row = extract_situation(filing) if i in picked else _blank(filing, "skipped_quota", "form_type_quota_exhausted")
            out.write(json.dumps(row, sort_keys=True) + "\n"); out.flush()
if __name__ == "__main__": main()
