# Boundaries of Retail Quantitative Trading on Prediction Markets

**Four gates, one new failure mode, 225 alternative routes — a map of where LLM-assisted retail prediction-market trading fails, drawn from 13 Abel AI Lab campaigns.**

[![Code License](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Docs & Data License](https://img.shields.io/badge/docs%20%26%20data-CC%20BY%204.0-green.svg)](LICENSE-DOCS)
[![Paper Eval](https://img.shields.io/badge/paper%20eval-100%2F100-brightgreen.svg)](code/eval/boundaries-of-retail-prediction-market-trading-eval.sh)
[![CI](https://img.shields.io/github/actions/workflow/status/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/eval-paper.yml?branch=main&label=CI)](https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/actions)

---

## The Result in One Paragraph

When LLMs meet retail prediction markets, four gates determine whether any route survives: **sourceability**, **fillability**, **capacity**, and **anchor stability**. Across 13 Abel AI Lab campaigns and 156 adversarial-review rounds we document each gate, name a cross-mechanism failure mode — **ceiling-pin layer migration**, the LLM-extraction defect that moves from the rubric layer to the prompt layer once the rubric is tightened (n=3 instances) — and formalize a pre-launch program-gate methodology that caught 18 of 21 launch defects before any implementation round began. The repository preserves 225 alternative routes with their selected, rejected, deferred, and promoted decisions, a 52-row strict-parsed attack registry, and a 40-quote verbatim evidence bank. The contribution is a **map of failure modes** for retail builders, a **methodology that generalizes beyond trading**, and a **failure-preserving corpus** for cross-validation. Bounded: single-lab, single-period; suggestive, not universal.

```
                campaigns ──┐
   164 round dirs (raw)     │   sources       gates           outcome
   ───────────────────      │   ───────       ─────           ───────
   17 raw campaigns         │   state.json    sourceability   keeps        45
   ─ 4 sparse legacy        ├─▶ peer files  ▶ fillability  ▶ rejected   135
   ─────────────────────    │   route reg.    capacity        deferred    45
   13 active campaigns      │   quote bank    anchor          promoted    82
   156 instrumented rounds  │   methodology  ─── 4 gates ───▶ ceiling-pin n=3
                            ┘                                 saturation: §4
                                                              capacity:   §6
                                                              anchoring:  §7
                                                              methodology:§8
```

## Get Started in Three Commands

```bash
git clone https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading.git
cd boundaries-of-retail-prediction-market-trading
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
# expect: paper_readiness_score=100.00 ; hard_gate_violations=[]
```

The eval script reads the paper, the data, and the references and prints a single readiness score plus a structured log. Score `≥85` and `hard_gate_violations=[]` is the public-release contract for this repository.

## Headline Numbers

| Result | Value | Source |
|---|---:|---|
| Sustainable >$1k/month retail trading routes found | **0** of 11 trading-focused campaigns | §4–§7 |
| Cross-mechanism LLM-extraction ceiling-pin instances | **n=3** (suggestive, not structural) | §5 |
| Math-arb mechanism saturation evidence | 327-trade arsenal closed; 0/4365 live violations | §4 |
| Smallest fillable book observed | $5.34 (23.6% spread, but only ~$5 of depth) | §6 |
| Anchor-induced prior drift in sister artifact | 256.73 probability bps (single LLM, single domain) | §7, MarketAnchor v0.1.2 |
| Round-0 program-gate defects caught pre-launch | 18→3→1→0 (Path C); 21→6→4→3→1 (Paper 2) | §8 |

## Corpus Composition

| Layer | Count | Status |
|---|---:|---|
| Raw campaign directories | 17 | Includes 4 sparse legacy |
| Active campaigns analyzed | 13 | 12 fully instrumented + 1 peer-files-only |
| Raw round directories | 164 | |
| Instrumented rounds | 156 | |
| Trading-focused rounds | 59 | Infrastructure rounds (97) used only for methodology |
| Verified arXiv references | 32 | Cross-validated via [reference-check workflow](.github/workflows/reference-check.yml) |
| Canonical journal references | 11 | DOI-verified via Crossref |
| Strict-parsed peer attacks | 52 | [data/anc/attack-registry.jsonl](data/anc/attack-registry.jsonl) |
| Alternative routes recorded | 225 | 45 selected / 135 rejected / 45 deferred / 82 promoted |
| Verbatim quote-bank rows | 40 | Per-campaign cap 8; peer-role cap 60% |

## Repository Layout

```
.
├── docs/main.md            ← the manuscript (1353 lines)
├── docs/references.bib     ← 44 BibTeX entries, all DOI/arXiv-verified
├── data/                   ← cross-campaign aggregate + ancillary registries
│   ├── cross-campaign-aggregate.json
│   ├── per-campaign-summary.csv
│   └── anc/                  attack registry, alternative routes,
│                             quote bank, methodology timeline,
│                             methodology self-attacks, recurring attacks
├── code/eval/              ← single-shell readiness check (Python stdlib)
├── code/extraction/        ← engineering primitives from a terminated campaign
└── .github/workflows/      ← CI: paper eval, markdown lint, reference check
```

The eval shell is intentionally small and dependency-free. The data directory is the source of truth; the manuscript reads from it. The extraction code is preserved as engineering reference, not as a working trading system.

## Reproduction

```bash
# 1. Static checks (stdlib only, no network)
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
python3 -m json.tool data/cross-campaign-aggregate.json >/dev/null

# 2. Reference resolution (requires network; arXiv API + Crossref API)
python3 - <<'PY'
import re, pathlib
bib = pathlib.Path("docs/references.bib").read_text()
print("arXiv IDs:", len(set(re.findall(r"arXiv:(\d{4}\.\d{4,5})", bib))))
print("DOIs:    ", len(set(re.findall(r"doi\s*=\s*\{([^}]+)\}", bib, re.I))))
PY

# 3. Corpus integrity
wc -l docs/main.md data/per-campaign-summary.csv data/anc/*.jsonl
```

Expected: 32 arXiv IDs, 11 DOIs, 1353 lines in `main.md`, 18 lines in the CSV, 52 attacks, 225 alternative routes, 21 methodology self-attacks, 40 quote-bank rows, 2 recurring-attacks rows.

The CI runs the same checks on every push to `main`. See the [Actions tab](https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/actions).

## What This Repository Is

A failure-preserving record of a retail prediction-market trading research program. The artifact contains the manuscript, every cited reference, the 17-row aggregate that defines the corpus, the strict-parsed attack registry, the 225-route alternative-routes ledger, a curated 40-quote evidence bank with verbatim grounding, and the methodology timeline that distinguishes pre-registered from retrospectively analyzed campaigns.

## What This Repository Is Not

It is not a trading bot, not financial advice, not a recommendation to trade on Polymarket, Kalshi, or any other venue. It does not claim universal market efficiency, universal LLM trading impossibility, or any institutional-scale result. The included extraction code documents engineering primitives from a campaign that was deliberately terminated; it is not a working automated desk. The sister MarketAnchor v0.1.2 manuscript is included only for narrow context on consensus-anchor sensitivity in a stored LLM forecasting run; it does not claim tradable edge.

## Sister Paper

[MarketAnchor v0.1.2](docs/sycophancy-benchmark-marketanchor-v0.1.2.md) measures consensus-anchor sensitivity in one stored prediction-market forecasting run. SHA256 `8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27`. Status: preprint, citation pending an external identifier.

## Citation

```bibtex
@misc{Wang2026BoundariesRetailQuantitativeTrading,
  title  = {Boundaries of Retail Quantitative Trading on Prediction Markets:
            A Multi-Mechanism Empirical Retrospective},
  author = {Wang, Stephen},
  year   = {2026},
  version = {v0.1.0},
  institution = {Abel AI Lab},
  url    = {https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading}
}
```

GitHub renders [CITATION.cff](CITATION.cff) for the cite-this-repository widget.

## Related Work

The full bibliography lives in [docs/references.bib](docs/references.bib). The retrospective draws on five strands — LLM forecasting, anchoring and sycophancy, financial LLMs and trading agents, prediction-market-specific evaluation, and survivorship and false-positive control — synthesized in §2 of the paper.

## License

Repository code under [Apache-2.0](LICENSE-CODE). Manuscript, data, and prose under [CC BY 4.0](LICENSE-DOCS). Both licenses are irrevocable.

## Contributing

Contributions that improve reproducibility, repair verifiable errors, or sharpen scope are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the issue templates for bug reports and methodology questions. Pull requests should keep the eval green and include the eval log when manuscript, data, citations, or code change.

## Author

Stephen Wang — Abel AI Lab — `lab@abel.ai`

The manuscript discloses AI/tool assistance directly: Anthropic Claude for peer-challenge critique and adversarial review, OpenAI Codex CLI gpt-5.5 for repository inspection, statistical recomputation, and drafting assistance. These tools are not authors.

## Changelog

The campaign moved through five round-0 program-gate iterations, four implementation rounds, a literary polish pass, and a related-work canonical-reference upgrade. See [CHANGELOG.md](CHANGELOG.md). Initial public release: v0.1.0, 2026-05-06.
