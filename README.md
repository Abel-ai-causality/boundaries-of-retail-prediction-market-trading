# Boundaries of Retail Quantitative Trading on Prediction Markets

Multi-campaign empirical evidence on where LLM-assisted retail prediction-market trading
routes failed under adversarial review at Abel AI Lab.

[![Code License](https://img.shields.io/badge/code%20license-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Docs/Data License](https://img.shields.io/badge/docs%20%26%20data-CC%20BY%204.0-green.svg)](LICENSE-DOCS)
[![DOI](https://img.shields.io/badge/DOI-Zenodo%20pending-lightgrey.svg)](.zenodo.json)
[![arXiv](https://img.shields.io/badge/arXiv-pending-lightgrey.svg)](docs/main.md)
[![Eval](https://img.shields.io/badge/eval-v0.1.0%20pending-lightgrey.svg)](code/eval/boundaries-of-retail-prediction-market-trading-eval.sh)

## TL;DR

This repository accompanies Paper 2 from Abel AI Lab: a single-lab,
single-period retrospective of LLM-assisted prediction-market trading campaigns.
The evidence maps a practical boundary: the obvious retail-scale routes that were
accessible to LLM tooling did not survive adversarial review as durable trading
systems in this corpus. The strongest claims are descriptive, not universal:
math-arbitrage saturation, capacity limits, ceiling-pin behavior in LLM extraction,
and anchoring uncertainty appear as observed constraints. The n=3 ceiling-pin
observations are suggestive cross-mechanism evidence, not a model-wide theorem.

## Table of Contents

- [What This Is](#what-this-is)
- [What This Is Not](#what-this-is-not)
- [Quick Stats](#quick-stats)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Reproduction Guide](#reproduction-guide)
- [The Paper](#the-paper)
- [Sister Paper](#sister-paper)
- [Citation](#citation)
- [Related Work](#related-work)
- [Contributing](#contributing)
- [License](#license)
- [Maintainers](#maintainers)
- [Acknowledgments](#acknowledgments)
- [Changelog](#changelog)
- [Contact](#contact)

## What This Is

This is a public-release package for the Paper 2 manuscript, data, and minimal
reproduction code.

It contains:

- the Paper 2 manuscript in [docs/main.md](docs/main.md);
- the 44-entry BibTeX bibliography in [docs/references.bib](docs/references.bib);
- cross-campaign aggregate data and ancillary registries in [data/](data/);
- a release-local eval shell in
  [code/eval/boundaries-of-retail-prediction-market-trading-eval.sh](code/eval/boundaries-of-retail-prediction-market-trading-eval.sh);
- Path C extraction primitives preserved as engineering reference in
  [code/extraction/](code/extraction/);
- citation, Zenodo, GitHub Actions, issue-template, and contribution metadata.

The empirical unit is not a single backtest. The corpus records Abelian research
rounds in which LLM-assisted systems proposed, mutated, attacked, and either
retained or terminated candidate trading routes.

The release is intended for reviewers who want to inspect the paper, reproduce
the static readiness checks, audit the extracted registries, and cite the artifact
once Stephen Wang confirms the license and public URLs.

## What This Is Not

This repository is not a trading bot.

It is not financial advice, investment advice, or a recommendation to trade on
Polymarket, Kalshi, or any other prediction-market venue.

It does not claim that all prediction markets are efficient, that all LLM trading
systems fail, or that no private-data or institutional route can work.

It does not provide a production execution stack, wallet management, broker
integration, market-making infrastructure, or risk-management software.

The Path C extraction code is included because it documents useful engineering
primitives from a terminated campaign. It is not a working automated special-
situation trading desk.

The MarketAnchor sister paper is included only for context on consensus-anchor
sensitivity. It is marked as preprint, citation pending until an external
identifier exists.

## Quick Stats

| Item | Value | Notes |
|---|---:|---|
| Active campaigns analyzed | 13 | Four sparse legacy directories retained only for denominator honesty |
| Raw campaign inventory | 17 | Stored in [data/cross-campaign-aggregate.json](data/cross-campaign-aggregate.json) |
| Instrumented rounds | 156 | Across the active corpus |
| Raw round directories | 164 | Includes sparse legacy inventory |
| Trading-focused rounds | 59 | Used for substantive trading findings after infrastructure down-weighting |
| Fully instrumented Abelian campaigns | 12 | State JSON and round artifacts available internally |
| Peer-files-only active campaign | 1 | Included with narrower evidentiary weight |
| Verified arXiv IDs | 32 | Cross-validated against [docs/references.bib](docs/references.bib) |
| BibTeX entries | 44 | Includes LLM, forecasting, market microstructure, and PM references |
| Ceiling-pin observations | n=3 | Cross-mechanism, single-lab, suggestive |
| Strict-parsed attack rows | 52 | [data/anc/attack-registry.jsonl](data/anc/attack-registry.jsonl) |
| Alternative routes | 225 | [data/anc/alternative-routes.jsonl](data/anc/alternative-routes.jsonl) |
| Quote-bank rows | 40 | Verbatim evidence snippets |
| Eval hard gates | 0 | On the copied v0.1.0 manuscript and data |
| Release version | v0.1.0 | Initial public-release package |

## Repository Structure

```text
.
├── README.md
├── LICENSE-CODE
├── LICENSE-DOCS
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── .gitignore
├── .zenodo.json
├── .github/
│   ├── workflows/
│   │   ├── markdown-lint.yml
│   │   ├── reference-check.yml
│   │   └── eval-paper.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.md
│   │   └── methodology-question.md
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── main.md
│   ├── references.bib
│   ├── retrospective-2026-05-04-05.md
│   └── sycophancy-benchmark-marketanchor-v0.1.2.md
├── data/
│   ├── cross-campaign-aggregate.json
│   ├── per-campaign-summary.csv
│   ├── anc/
│   │   ├── attack-registry.jsonl
│   │   ├── recurring-attacks.csv
│   │   ├── alternative-routes.jsonl
│   │   ├── methodology-self-attacks.jsonl
│   │   ├── quote-bank.jsonl
│   │   └── methodology-timeline.md
│   └── README.md
├── code/
│   ├── eval/
│   │   └── boundaries-of-retail-prediction-market-trading-eval.sh
│   ├── extraction/
│   │   ├── __init__.py
│   │   ├── edgar_scanner.py
│   │   ├── extract.py
│   │   └── scoring.py
│   └── README.md
├── pyproject.toml
└── requirements.txt
```

## Installation

The static reproduction path uses Python 3.11+ and standard-library tooling.
No Python package dependency is required for the main eval.

```bash
git clone https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading.git
cd boundaries-of-retail-prediction-market-trading
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependency notes:

- the eval shell uses `bash` and `python3`;
- the data checks use Python standard-library modules only;
- the EDGAR scanner uses Python standard-library networking;
- the historical Path C extractor can call the Codex CLI if run directly;
- `cffconvert` is optional for local validation of [CITATION.cff](CITATION.cff).

## Quick Start

Run the core checks:

```bash
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
cat .eval/rbaseline-eval.log
python3 -m json.tool data/cross-campaign-aggregate.json >/tmp/paper2.aggregate.json
python3 - <<'PY'
import pathlib, re
text = pathlib.Path("docs/references.bib").read_text(encoding="utf-8")
print(len(re.findall(r"^@", text, re.MULTILINE)))
PY
wc -l docs/main.md docs/references.bib data/per-campaign-summary.csv data/anc/*.jsonl
```

Expected static eval output for v0.1.0:

```text
paper_readiness_score=100.00
hard_gate_violations=[]
verified=32
unverified_extras=0
data_schema_valid=True
```

## Reproduction Guide

The static reproduction path is intentionally small.

```bash
test -f docs/main.md
test -f docs/references.bib
python3 -m json.tool data/cross-campaign-aggregate.json >/tmp/paper2.aggregate.json
python3 - <<'PY'
import json
rows = json.load(open("data/cross-campaign-aggregate.json", encoding="utf-8"))
print(len(rows))
PY
wc -l data/per-campaign-summary.csv
wc -l data/anc/attack-registry.jsonl \
  data/anc/alternative-routes.jsonl \
  data/anc/methodology-self-attacks.jsonl \
  data/anc/quote-bank.jsonl \
  data/anc/recurring-attacks.csv
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
```

Expected values are 17 aggregate rows, 18 CSV lines, 52 attacks, 225 alternative
routes, 21 methodology self-attacks, 40 quote-bank rows, and 2 recurring-attack
CSV lines. The eval should show `paper_readiness_score >= 85` and
`hard_gate_violations=[]`; the v0.1.0 copy scores 100.00. Re-run the same checks
after any manuscript, reference, data, or eval change.

## The Paper

Paper: [docs/main.md](docs/main.md)

ArXiv: pending

Zenodo DOI: pending

Abstract:

> When a single research lab tries to turn LLM-accessible market information
> into deployable retail trading on prediction markets, where do the routes
> fail?

The paper answers from 13 active campaigns and 156 instrumented rounds at
Abel AI Lab in 2026-Q2. It reports four mechanisms: math-arbitrage saturation,
cross-mechanism LLM-extraction ceiling-pin behavior, retail-bankroll capacity
ceilings, and anchoring uncertainty as a trading constraint. The claims are
bounded to the observed corpus and should be treated as a map of failure modes,
not as a universal impossibility result.

## Sister Paper

Sister paper:
[docs/sycophancy-benchmark-marketanchor-v0.1.2.md](docs/sycophancy-benchmark-marketanchor-v0.1.2.md)

Status: preprint, citation pending.

Construct: consensus-anchor sensitivity in a stored prediction-market
forecasting run.

SHA256:

```text
8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27
```

Paper 2 cites MarketAnchor v0.1.2 only for the narrower observation that a
stored LLM forecasting run moved under consensus-framed anchors. It does not
treat that statistic as tradable edge, realized return, or calibration error.

## Citation

BibTeX:

```bibtex
@misc{Wang2026BoundariesLLMPM,
  title = {Boundaries of Retail Quantitative Trading on Prediction Markets:
           A Multi-Mechanism Empirical Retrospective},
  author = {Wang, Stephen},
  year = {2026},
  version = {v0.1.0},
  institution = {Abel AI Lab},
  doi = {10.5281/zenodo.0000000},
  url = {https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading},
  note = {DOI and arXiv placeholders pending public release}
}
```

APA:

Wang, S. (2026). *Boundaries of Retail Quantitative Trading on Prediction
Markets: A Multi-Mechanism Empirical Retrospective* (Version
v0.1.0). Abel AI Lab. https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading

Plain text:

Stephen Wang, "Boundaries of Retail Quantitative Trading on Prediction
Markets," Abel AI Lab, v0.1.0, 2026.

GitHub also reads [CITATION.cff](CITATION.cff) for the citation widget.

## Related Work

The full bibliography is in [docs/references.bib](docs/references.bib).

Key references used by the paper include:

- Ouyang et al. (2022), instruction-following language models with human feedback.
- Bai et al. (2022), Constitutional AI.
- Perez et al. (2022), model-written evaluations.
- Sharma et al. (2023), sycophancy in language models.
- Karger et al. (2024), ForecastBench.
- Lou and Sun (2024), anchoring bias in large language models.
- Schoenegger et al. (2024), AI-augmented human forecasting.
- Wolfers and Zitzewitz (2004), prediction markets.
- Glosten and Milgrom (1985), bid, ask, and transaction prices.
- Bailey and Lopez de Prado (2014), deflated Sharpe ratio and selection bias.

## Contributing

Contributions are welcome when they improve reproducibility, clarify scope, or
repair verifiable errors.

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Please use the issue templates
for bug reports and methodology questions, keep pull requests small, and include
the eval output if a change touches manuscript, data, citations, or code.

## License

Proposed default before public push:

- code: Apache License 2.0, see [LICENSE-CODE](LICENSE-CODE);
- paper, docs, and data: Creative Commons Attribution 4.0 International, see
  [LICENSE-DOCS](LICENSE-DOCS).

Stephen Wang and Abel AI Lab must confirm these choices before public release.
The license files intentionally include placeholder notices at the top.

## Maintainers

- Stephen Wang, Abel AI Lab, <lab@abel.ai>
- `github.com/Abel-ai-causality`
- `boundaries-of-retail-prediction-market-trading`

## Acknowledgments

The manuscript discloses AI/tool assistance directly. Anthropic Claude was used
for peer-challenge critique, framing review, and adversarial policy review.
OpenAI Codex CLI gpt-5.5 was used for repository inspection, statistical
recomputation support, transcript mining, reference checks, and drafting
assistance. These tools are not authors.

External editorial and methodological feedback improved metric naming, protocol
stratification, contract-cluster sensitivity analysis, and related-work coverage.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the R0 through R4 campaign history, polish
pass, and RW-canonical reference pass.

The initial public release is v0.1.0 and reflects the internal Abelian campaign
state as of 2026-05-06.

## Contact

For paper, data, and reproduction questions:

- email: <lab@abel.ai>
- GitHub issues: <https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/issues>

Use the methodology-question template when referencing a specific finding,
campaign, quote-bank row, or attack-registry row.
