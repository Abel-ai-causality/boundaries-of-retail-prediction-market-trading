import argparse, json, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET
UA = "Stephen Wang (Abel AI Lab) lab@abel.ai"; ENDPOINT = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type={}&owner=include&count={}&output=atom"
def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        data = urllib.request.urlopen(req, timeout=30).read()
    except urllib.error.HTTPError as e:
        if e.code != 429: raise
        time.sleep(5); data = urllib.request.urlopen(req, timeout=30).read()
    time.sleep(0.15); return data
def fetch_daily_filings(form_type: str, count: int = 40) -> list[dict]:
    root = ET.fromstring(_get(ENDPOINT.format(urllib.parse.quote(form_type), count))); ns = {"a": "http://www.w3.org/2005/Atom"}; rows = []
    for ent in root.findall("a:entry", ns):
        summary = (ent.findtext("a:summary", "", ns) or "").replace("\n", " ")
        if form_type == "8-K" and ("Item 1.01" not in summary or "Item 2.01" in summary): continue
        title = ent.findtext("a:title", "", ns); link = ent.find("a:link", ns).attrib.get("href", "")
        acc = (ent.findtext("a:id", "", ns).rsplit("=", 1)[-1] or summary.split("AccNo:</b>", 1)[-1].split("<", 1)[0].strip())
        filed = summary.split("Filed:</b>", 1)[-1].split("<", 1)[0].strip()[:10]
        filer = title.split(" - ", 1)[-1].rsplit(" (", 2)[0]; doc = link.rsplit("/", 1)[0] + "/" + acc + ".txt"
        rows.append({"accession_no": acc, "filer": filer, "form_type": form_type, "filed_date": filed, "primary_doc_url": doc, "summary_text": summary, "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    return rows
def main():
    p = argparse.ArgumentParser(); p.add_argument("--forms", required=True); p.add_argument("--output", required=True); p.add_argument("--count", type=int, default=40); a = p.parse_args()
    with open(a.output, "w") as out:
        for form in [f.strip() for f in a.forms.split(",") if f.strip()]:
            rows = fetch_daily_filings(form, a.count); print(f"{form}\t{len(rows)}")
            for row in rows: out.write(json.dumps(row, sort_keys=True) + "\n")
if __name__ == "__main__": main()
