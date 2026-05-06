#!/bin/bash
# Paper 2 retrospective eval (v3) — content_sections + JSON schema validation + banned-phrase guard + unverified-citation penalty
# Targets: ≥1000 lines / ≥7 content_sections (admin excluded) / ≥25 verified citations / 0 unverified extras / 0 banned phrases
# AI disclosure must name Claude AND Codex; Reproducibility appendix must embed v0.1.2 SHA256
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
ROUND="${ABELIAN_ROUND:-baseline}"
RUN_DIR="${ABELIAN_RUN_DIR:-$REPO_ROOT/.eval}"
PAPER="${PAPER:-$REPO_ROOT/docs/main.md}"
DATA="${DATA:-$REPO_ROOT/data/cross-campaign-aggregate.json}"
REFS="${REFS:-$REPO_ROOT/docs/references.bib}"
EVAL_LOG="$RUN_DIR/r${ROUND}-eval.log"
EVAL_ERR="$RUN_DIR/r${ROUND}-eval-err.log"
V012_SHA="8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27"

mkdir -p "$RUN_DIR"

if [ ! -f "$PAPER" ]; then
    printf "0.00\n"
    {
        echo "=== Paper 2 retrospective eval v3 (baseline / no main.md) ==="
        echo "paper_readiness_score=0.00"
        echo "note=main.md absent — returning baseline 0"
    } >"$EVAL_LOG"
    exit 0
fi

PAPER="$PAPER" DATA="$DATA" REFS="$REFS" EVAL_LOG="$EVAL_LOG" V012_SHA="$V012_SHA" python3 <<'PYEOF' 2>"$EVAL_ERR"
import json
import os
import re

paper_path = os.environ["PAPER"]
data_path = os.environ["DATA"]
refs_path = os.environ["REFS"]
eval_log = os.environ["EVAL_LOG"]
v012_sha = os.environ["V012_SHA"]

with open(paper_path, encoding="utf-8") as f:
    paper = f.read()

lines = paper.count("\n") + (0 if paper.endswith("\n") else 1)

# Content sections: total ## headings minus admin-pattern headings
all_sections = re.findall(r"^##\s+(.+)$", paper, re.MULTILINE)
admin_pattern = re.compile(
    r"^(?:AI\s+(?:and\s+Tool|Tool)\s+Assistance\s+Disclosure|"
    r"Acknowledg|References|Reproducibility|Appendix|License|"
    r"AI\s+Disclosure|Foreword)",
    re.IGNORECASE,
)
content_sections = [s for s in all_sections if not admin_pattern.match(s.strip())]
n_total_sections = len(all_sections)
n_content_sections = len(content_sections)

# Citations: cross-validate main.md arXiv IDs against references.bib
paper_arxiv_ids = set(re.findall(r"arXiv:(\d{4}\.\d{4,5})", paper))
refs_arxiv_ids = set()
if os.path.exists(refs_path):
    with open(refs_path, encoding="utf-8") as f:
        refs_text = f.read()
    matches = re.findall(r"arXiv:(\d{4}\.\d{4,5})|arxiv\.org/abs/(\d{4}\.\d{4,5})", refs_text)
    refs_arxiv_ids = {x for tup in matches for x in tup if x}
verified_arxiv_ids = paper_arxiv_ids & refs_arxiv_ids
verified_count = len(verified_arxiv_ids)
unverified_count = len(paper_arxiv_ids - refs_arxiv_ids)

# AI disclosure check: requires Claude AND Codex AND "These tools are not authors"
ai_disclosure_full = (
    bool(re.search(r"AI and Tool Assistance Disclosure", paper))
    and bool(re.search(r"These tools are not authors", paper))
    and bool(re.search(r"\bClaude\b", paper))
    and bool(re.search(r"\bCodex\b", paper))
)
reproducibility_full = bool(re.search(r"## Reproducibility", paper)) and (v012_sha in paper)

# Banned-phrase guard (c3.3): paper must NOT contain overclaim phrases
banned_phrases = [
    r"we discover\b",
    r"we are first to find",
    r"frontier of AI trading",
    r"we discovered",
    r"first to discover",
]
banned_hits = sum(1 for p in banned_phrases if re.search(p, paper, re.IGNORECASE))

# Padding/repetition guard (R2 catch 2026-05-06): paper must not pad to hit line target
# via verbatim paragraph repetition. Compute paragraph uniqueness ratio.
# Paragraphs = blocks separated by 2+ newlines. Strip leading "N:" / "Note N:" patterns
# so codex's "Diagnostic 1:", "Diagnostic 2:", ... numeric variations are detected.
paragraphs_raw = [p.strip() for p in re.split(r"\n\s*\n", paper) if p.strip()]
def normalize_for_uniqueness(p):
    # Strip leading enumeration patterns up to 4 words + number + colon/period:
    # "Diagnostic N:", "Methodology note N:", "Ceiling-pin diagnostic N:",
    # "Section 5.1.N:", "Pattern N:", "Lemma N.", "Note N.", etc.
    p = re.sub(r"^(?:[A-Za-z][A-Za-z\-]*\s+){0,4}\d+(?:\.\d+)?\s*[:\.\)]\s+", "", p)
    # Collapse whitespace
    p = re.sub(r"\s+", " ", p).strip()
    # Use fingerprint = first 60 chars + last 60 chars to catch variations both ends
    if len(p) >= 120:
        return p[:60] + "|||" + p[-60:]
    return p
paragraphs_normalized = [normalize_for_uniqueness(p) for p in paragraphs_raw]
n_paragraphs = len(paragraphs_normalized)
n_unique = len(set(paragraphs_normalized))
uniqueness_score = n_unique / n_paragraphs if n_paragraphs > 0 else 1.0

# Cross-campaign data validation: grep both literals + JSON schema check
cross_campaign_grep = ("13 active campaigns" in paper) and ("156 instrumented rounds" in paper)
data_file_present = os.path.exists(data_path)
data_schema_valid = False
n_campaigns_in_data = 0
allowed_instrumentation = {"full_state_json", "peer_files_only", "empty_legacy"}
if data_file_present:
    try:
        with open(data_path, encoding="utf-8") as f:
            data_obj = json.load(f)
        rows = None
        if isinstance(data_obj, list):
            rows = data_obj
        elif isinstance(data_obj, dict) and "campaigns" in data_obj and isinstance(data_obj["campaigns"], list):
            rows = data_obj["campaigns"]
        if rows is not None:
            n_campaigns_in_data = len(rows)
            required_keys = {"run_id", "instrumentation_level"}
            data_schema_valid = (
                n_campaigns_in_data >= 17
                and all(
                    isinstance(r, dict)
                    and required_keys.issubset(set(r.keys()))
                    and r.get("instrumentation_level") in allowed_instrumentation
                    and isinstance(r.get("run_id"), str)
                    and len(r.get("run_id", "")) > 0
                    for r in rows
                )
            )
    except (json.JSONDecodeError, OSError, KeyError, TypeError):
        data_schema_valid = False

data_complete = cross_campaign_grep and data_file_present and data_schema_valid

# Weighted score 0-100
line_score = min(lines / 1000.0, 1.0) * 30
section_score = min(n_content_sections / 7.0, 1.0) * 20

# Citation score with unverified-extras penalty
citation_score = min(verified_count / 25.0, 1.0) * 20
if unverified_count > 0:
    # penalize: subtract up to 50% of citation_score for any unverified extras
    citation_score *= max(0.5, 1.0 - 0.1 * unverified_count)

# Data score: full only if grep + file + schema valid; partial if 2/3
if data_complete:
    data_score = 15
elif sum([cross_campaign_grep, data_file_present, data_schema_valid]) == 2:
    data_score = 10
elif cross_campaign_grep or data_file_present:
    data_score = 5
else:
    data_score = 0

# Disclosure score
disclosure_score = (7.5 if ai_disclosure_full else 0) + (7.5 if reproducibility_full else 0)

# Banned-phrase penalty: subtract from disclosure_score (severe — overclaim is publishability blocker)
if banned_hits > 0:
    disclosure_score = max(0, disclosure_score - 5 * banned_hits)

total = line_score + section_score + citation_score + data_score + disclosure_score

# HARD GATES — cap total at 75 (below 85 goal-met threshold) on contract-violations.
# ZERO TOLERANCE policy: any single contract violation caps the score below threshold.
# Eval REFUSES to certify a contract-violating paper, not merely soft-penalize.
hard_gate_violations = []
if banned_hits > 0:
    hard_gate_violations.append(f"banned_phrase_hits={banned_hits}")
if unverified_count > 0:
    hard_gate_violations.append(f"unverified_extras={unverified_count}>0")
if data_file_present and not data_schema_valid:
    hard_gate_violations.append("data_schema_invalid")
if uniqueness_score < 0.85:
    hard_gate_violations.append(f"paragraph_uniqueness={uniqueness_score:.3f}<0.85")
# Note: data file ABSENCE is not a hard violation (R0 baseline + early R1 stub OK);
# only INVALID schema when present is a contract violation.
if hard_gate_violations:
    total = min(total, 75.0)

with open(eval_log, "w", encoding="utf-8") as log:
    log.write("=== Paper 2 retrospective eval v3 ===\n")
    log.write(f"paper_lines={lines} total_sections={n_total_sections} content_sections={n_content_sections}\n")
    log.write(f"paper_arxiv_ids={len(paper_arxiv_ids)} refs_arxiv_ids={len(refs_arxiv_ids)} verified={verified_count} unverified_extras={unverified_count}\n")
    log.write(f"ai_disclosure_full={ai_disclosure_full} reproducibility_with_v012_sha={reproducibility_full}\n")
    log.write(f"cross_campaign_grep={cross_campaign_grep} data_file_present={data_file_present} data_schema_valid={data_schema_valid} n_campaigns_in_data={n_campaigns_in_data}\n")
    log.write(f"banned_phrase_hits={banned_hits} n_paragraphs={n_paragraphs} n_unique={n_unique} uniqueness_score={uniqueness_score:.3f}\n")
    log.write(f"line_score={line_score:.2f} section_score={section_score:.2f} citation_score={citation_score:.2f}\n")
    log.write(f"data_score={data_score:.2f} disclosure_score={disclosure_score:.2f}\n")
    log.write(f"hard_gate_violations={hard_gate_violations}\n")
    log.write(f"paper_readiness_score={total:.2f}\n")

print(f"{total:.2f}")
PYEOF
