# Legibility Is Not Deployability

**Four Gates for LLM-Assisted Prediction-Market Trading.**
A failure-preserving Abel AI Lab corpus from 2026-Q2 — 13 campaigns, 156 adversarial-review rounds, 225 route decisions — and a NeurIPS-style manuscript that maps where model-readable routes lose the right to be called trades.

[![Code License](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Docs & Data License](https://img.shields.io/badge/docs%20%26%20data-CC%20BY%204.0-green.svg)](LICENSE-DOCS)
[![Manuscript](https://img.shields.io/badge/manuscript-v0.2.0-brightgreen.svg)](docs/main.md)
[![CI](https://img.shields.io/github/actions/workflow/status/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/eval-paper.yml?branch=main&label=CI)](https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/actions)

---

## The Result in One Paragraph

When LLMs meet retail prediction markets, four operational gates decide whether any apparent edge becomes a trade: **sourceability**, **fillability**, **capacity**, and **anchor stability**. Across 13 active Abel AI Lab campaigns and 156 instrumented adversarial-review rounds, **zero** routes cleared all four gates strongly enough to support a durable greater-than-$1k/month retail deployment claim. The paper formalizes a cross-mechanism failure mode — **ceiling-pin layer migration**, in which an LLM-extraction defect survives a rubric repair by relocating from the scoring layer to the prompt/output layer (n=2 strict, n=3 prompt-gate family) — and documents an adversarial **R0 program gate** that made launch ambiguity countable before any implementation round began (Path C: 18 → 3 → 1 → 0; Manuscript: 21 → 6 → 4 → 3 → 1). The corpus preserves 225 route decisions (45 selected / 135 rejected / 45 deferred; 79 also flagged `promoted_to_next_round`), 52 strict-parsed attacks, and 40 verbatim quote rows alongside an Evidence Locator that maps every numeric claim to its source artifact. The contribution is a **map of failure modes** for retail builders, an **adversarial protocol** that generalizes beyond trading, and a **failure-preserving corpus** that other labs can replicate against. Bounded: single-lab, single-period, suggestive — not universal.

```
                              ┌──────────────────────────────────────────────┐
   17 raw campaign dirs ─────▶│  G1 sourceability   external object verified │
    ─ 4 sparse legacy         │  G2 fillability     executable depth + time  │
   ─────────────────────      │  G3 capacity        $·E_j after fees, slip   │
   13 active campaigns        │  G4 anchor stab.    quote-masked LLM prior   │
   156 instrumented rounds    └──────────────────────────────────────────────┘
   225 routes (45/135/45/82)             │   ceiling-pin layer migration
   52 strict attacks                     │   (rubric → prompt; n=2 strict / n=3 family)
   40 verbatim quote rows                ▼
                                         0 durable >$1k/month retail routes
```

## Get Started in Three Commands

```bash
git clone https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading.git
cd boundaries-of-retail-prediction-market-trading
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
# expect: paper_readiness_score >= 85 ; hard_gate_violations=[]
```

The eval is a release-contract sanity check, not a quality judge: it verifies the manuscript shape, the AI-disclosure block, the cross-paper SHA cross-citation, banned-phrase absence, paragraph uniqueness, and the JSON corpus schema. Substantive paper review is done **by reading `docs/main.md`** and cross-checking claims against `docs/evidence-locator.md`.

## Headline Numbers

| Result                                                                  | Value                                       | Source                  |
| ----------------------------------------------------------------------- | ------------------------------------------: | ----------------------- |
| Durable >$1k/month retail trading routes                                | **0** of 11 trading-focused campaigns       | §4–§7                   |
| Cross-mechanism LLM-extraction ceiling-pin instances                    | **n=2 strict, n=3 prompt-gate family**      | §5, §10                 |
| Math-arb mechanism saturation evidence                                  | 327-trade arsenal closed; 0/4365 violations | §4                      |
| Smallest fillable book observed                                         | $5.34 (23.6% spread, ~$5 of NO depth)       | §6                      |
| Anchor-induced prior drift in sister artifact (MarketAnchor v0.1.2)     | 256.73 probability bps                      | §7, sister artifact     |
| R0 program-gate defects caught pre-launch (Path C)                      | 18 → 3 → 1 → 0                              | §8                      |
| R0 program-gate defects caught pre-launch (Manuscript)                  | 21 → 6 → 4 → 3 → 1                          | §8                      |
| Capacity verified shadow-only (pm-10k50k-profit, 4 candidates)          | $85,446.78 cumulative-to-50bps              | §6                      |

## Corpus Composition

| Layer                         |   Count | Status                                                 |
| ----------------------------- | ------: | ------------------------------------------------------ |
| Raw campaign directories      |      17 | 4 sparse legacy retained for inventory honesty         |
| Active campaigns analyzed     |      13 | 12 full state JSON + peer artifacts; 1 peer-files-only |
| Raw round directories         |     164 | Pre-partition                                          |
| Instrumented rounds (active)  |     156 | 97 infrastructure / 59 trading-focused                 |
| Trading-focused campaigns     |      11 | Mechanism-class partition in `data/anc/methodology-timeline.md` |
| Recovered route decisions     |     225 | 45 selected / 135 rejected / 45 deferred               |
| Promoted routes (`promoted_to_next_round`) | 79 | Carried-forward into next round's candidate pool       |
| Strict-parsed peer attacks    |      52 | After noisy earlier parse quarantined                  |
| Methodology self-attacks      |      21 | Manuscript-construction objections (separated)         |
| Verbatim quote-bank rows      |      40 | Per-campaign cap 8; peer-role cap 60%                  |
| References cited inline       |      12 | 4 arXiv + 8 journal; verifiable via `docs/references.bib` |

## Repository Layout

```
.
├── docs/
│   ├── main.md                                         the manuscript (Markdown)
│   ├── evidence-locator.md                             every numeric claim ↔ source artifact
│   ├── references.bib                                  12 cited references
│   ├── retrospective-2026-05-04-05.md                  campaign retrospective (supplementary)
│   └── sycophancy-benchmark-marketanchor-v0.1.2.md     sister-artifact full text
├── latex/
│   ├── main.tex                                        manuscript LaTeX (Overleaf-ready)
│   ├── main.pdf                                        compiled PDF
│   ├── figures/                                        6 figures (PDF + PNG)
│   ├── references.bib                                  copy of docs/references.bib for natbib
│   ├── compile.sh                                      pdflatex + bibtex + 2× pdflatex
│   └── Makefile, README.md
├── data/
│   ├── cross-campaign-aggregate.json                   17-row corpus card source
│   ├── per-campaign-summary.csv                        18-line summary (header + 17 rows)
│   └── anc/
│       ├── alternative-routes.jsonl                    225 route decisions
│       ├── attack-registry.jsonl                       52 strict-parsed peer attacks
│       ├── quote-bank.jsonl                            40 verbatim quotes
│       ├── methodology-self-attacks.jsonl              21 manuscript self-attacks
│       ├── methodology-timeline.md                     campaign partition rationale
│       └── recurring-attacks.csv                       cross-campaign recurrence
├── code/
│   ├── eval/                                           single-shell readiness check
│   └── extraction/                                     engineering primitives (terminated campaign)
└── .github/workflows/                                  CI: paper eval, markdown lint, reference check
```

The eval shell is intentionally small and dependency-free. The data directory is the source of truth; the manuscript reads from it. The extraction code is preserved as engineering reference, not as a working trading system.

## Reproduction

```bash
# 1. Static checks (stdlib only, no network)
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
python3 -m json.tool data/cross-campaign-aggregate.json >/dev/null

# 2. Corpus integrity
wc -l docs/main.md data/per-campaign-summary.csv data/anc/*.jsonl

# 3. Compile the LaTeX (TeX Live 2022+ or MikTeX)
( cd latex && bash compile.sh )

# 4. Cross-check headline claims against evidence-locator.md
grep -F '256.73' docs/sycophancy-benchmark-marketanchor-v0.1.2.md
python3 -c "import json,collections; \
  print(dict(collections.Counter(json.loads(l)['ultimate_outcome'] \
  for l in open('data/anc/alternative-routes.jsonl') if l.strip())))"
# expect: {'rejected': 135, 'selected': 45, 'deferred': 45}
```

The CI runs the static checks on every push to `main`. See the [Actions tab](https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/actions). The Evidence Locator (`docs/evidence-locator.md`) maps each manuscript claim to a runnable verification — read the paper, then audit any number directly.

## What This Repository Is

A failure-preserving record of a retail prediction-market trading research program. The artifact contains the manuscript, every cited reference, the 17-row aggregate that defines the corpus, the strict-parsed attack registry, the 225-route alternative-routes ledger, a curated 40-quote evidence bank with verbatim grounding, and the methodology timeline that distinguishes pre-registered from retrospectively analyzed campaigns.

## What This Repository Is Not

It is not a trading bot, not financial advice, not a recommendation to trade on Polymarket, Kalshi, or any other venue. It does not claim universal market efficiency, universal LLM trading impossibility, or any institutional-scale result. The included extraction code documents engineering primitives from a campaign that was deliberately terminated; it is not a working automated desk. The sister MarketAnchor v0.1.2 manuscript is included only for narrow context on consensus-anchor sensitivity in a stored LLM forecasting run; it does not claim tradable edge.

## Sister Paper

[MarketAnchor v0.1.2](docs/sycophancy-benchmark-marketanchor-v0.1.2.md) measures consensus-anchor sensitivity in one stored prediction-market forecasting run. SHA-256 `8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27`. The 256.73-bps anchor-drift result cited in §7 of this paper is reproduced from that frozen artifact.

## Citation

```bibtex
@misc{AbelAILab2026LegibilityNotDeployability,
  title       = {Legibility Is Not Deployability:
                 Four Gates for {LLM}-Assisted Prediction-Market Trading},
  author      = {{Abel AI Lab}},
  year        = {2026},
  version     = {v0.2.0},
  institution = {Abel AI Lab},
  url         = {https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading}
}
```

GitHub renders [CITATION.cff](CITATION.cff) for the cite-this-repository widget.

## Related Work

The bibliography lives in [docs/references.bib](docs/references.bib) (12 entries). The paper engages directly with five strands of prior work:

1. **Prediction-market microstructure** — Wolfers and Zitzewitz (2004), Manski (2006), Glosten and Milgrom (1985)
2. **AI forecasting benchmarks** — Karger et al. (2024) ForecastBench; Cheng et al. (2026) PolyBench; Schoenegger et al. (2024) AI-augmented predictions
3. **Anchoring and prior contamination** — Lou and Sun (2024)
4. **Survivorship and backtest overfitting** — Brown et al. (1992); Bailey and Lopez de Prado (2014)
5. **Pre-registration and adversarial methodology** — Nosek et al. (2018); Munafò et al. (2017); Perez et al. (2022)

Each reference is engaged inline in the body, not just listed.

## License

Repository code under [Apache-2.0](LICENSE-CODE). Manuscript, data, and prose under [CC BY 4.0](LICENSE-DOCS). Both licenses are irrevocable.

## Contributing

Contributions that improve reproducibility, repair verifiable errors, or sharpen scope are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the issue templates for bug reports and methodology questions. Pull requests should keep the eval green and include the eval log when manuscript, data, citations, or code change.

## Author

Abel AI Lab — `lab@abel.ai`

The manuscript discloses AI/tool assistance directly: Anthropic Claude for peer-challenge critique and adversarial review, OpenAI Codex CLI gpt-5.5 for repository inspection, statistical recomputation, and drafting assistance, and OpenAI ChatGPT for editorial revision. These tools are not authors.

## Changelog

v0.2.0 (2026-05-06) — title and structure rewrite to "Legibility Is Not Deployability", inline-cited references, formal Definitions 1–3 + capacity equation, six-figure NeurIPS layout, supplementary Evidence Locator. v0.1.0 (2026-05-06) — initial public release as "Boundaries of Retail Quantitative Trading on Prediction Markets". Full history in [CHANGELOG.md](CHANGELOG.md).
