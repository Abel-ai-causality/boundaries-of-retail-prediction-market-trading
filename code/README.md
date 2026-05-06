# Code Dictionary

This directory contains minimal code artifacts for Paper 2 reproduction and
engineering context.

## Runtime

Target Python: 3.11+

Python dependencies: none for the main release eval. The included Python scripts
use standard-library modules.

External tools:

- `bash` for the paper eval shell;
- optional `codex` CLI for the historical Path C extractor if run directly;
- optional network access for the EDGAR scanner and GitHub reference workflow.

## `eval/boundaries-of-retail-prediction-market-trading-eval.sh`

Usage:

```bash
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
cat .eval/rbaseline-eval.log
```

The eval checks:

- manuscript line count;
- content-section count;
- verified arXiv citation count;
- absence of unverified arXiv extras;
- AI/tool disclosure requirements;
- MarketAnchor v0.1.2 SHA256 in the reproducibility appendix;
- banned overclaim phrases;
- paragraph uniqueness;
- cross-campaign data schema.

Release gate:

```text
paper_readiness_score >= 85
hard_gate_violations=[]
```

The copied eval script resolves paths relative to the repository root. Override
`PAPER`, `DATA`, `REFS`, `ABELIAN_RUN_DIR`, or `ABELIAN_ROUND` only for local
experiments.

## `extraction/edgar_scanner.py`

Path C engineering primitive.

This script polls the SEC current-filings Atom endpoint for selected form types
and emits filing rows as JSONL. It uses a named SEC User-Agent and standard
library networking.

Example:

```bash
PYTHONPATH=code python3 -m extraction.edgar_scanner \
  --forms "8-K,SC TO-T" \
  --count 20 \
  --output /tmp/pathc-filings.jsonl
```

## `extraction/extract.py`

Path C engineering primitive from a terminated campaign.

The script reads filing rows, chunks long filing text, prompts an LLM extractor,
validates JSON shape, computes confidence, and writes JSONL output. The campaign
terminated because rubric-scored extraction remained vulnerable to ceiling-pin
and hallucinated evidence. This file is preserved as reference code, not as a
working trading system.

Historical execution may call the `codex` CLI and write prompt logs. Review the
paths and cost implications before running it.

## `extraction/scoring.py`

Path C confidence-scoring primitive.

The scorer awards confidence points for:

- recognized deal type;
- cash or stock consideration;
- plausible close-date distance from filing date;
- recognized regulatory-clearance field;
- recognized financing field.

The paper discusses why this style of rubric can over-score fabricated fields
unless each accepted field is grounded back to source text.

## License

Proposed license before public push: Apache License 2.0 for code. Stephen Wang
and Abel AI Lab confirm the final code license before release.
