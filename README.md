# Legibility Is Not Deployability

> An LLM can read every Polymarket contract. We tried 11 trading systems on a real prediction-market book.
> **Zero cleared the four gates that turn "I can read the price" into "I can trade the price."**
>
> Here is the failure-preserving record — every campaign, every rejected route, every attack — so you don't have to repeat it.

[![Code License](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Docs & Data License](https://img.shields.io/badge/docs%20%26%20data-CC%20BY%204.0-green.svg)](LICENSE-DOCS)
[![Manuscript](https://img.shields.io/badge/manuscript-v0.2.0-brightgreen.svg)](docs/main.md)
[![CI](https://img.shields.io/github/actions/workflow/status/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/eval-paper.yml?branch=main&label=CI)](https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading/actions)

---

## TL;DR

Two quarters. **13 campaigns. 156 adversarial-review rounds. 225 route decisions. 0 deployable.**

Reading a prediction market is not trading a prediction market. The gap has a shape. We named it.

| | What it asks | What kills it on Polymarket today |
|---|---|---|
| **G1 Sourceability** | Can the model verify the answer against an external object, or is it just a plausible string? | Fluent extraction with no source-grounded discriminator. |
| **G2 Fillability** | If you click buy, will the order actually fill? | Visible spreads evaporate under executable depth, fees, and slippage. |
| **G3 Capacity** | How many dollars survive after the fee? | Smallest filled book we found: **$5.34** at a 23.6% spread. |
| **G4 Anchor stability** | Is the LLM's prior independent of the market price? | Prior drifts **256.73 bps** when the consensus anchor leaks in. |

A route has to clear all four. Across 11 trading-focused campaigns, **none did**.

## Three takeaways, no hedge

**1. Reading a market is not trading a market.**
13 campaigns. 156 adversarial-review rounds. 225 route decisions. **0 deployable.** The four gates — sourceability, fillability, capacity, anchor stability — are not optional pipeline steps. They are the floor that turns a plausible-looking trade into a real one.

**2. Tighten the rubric and the bug doesn't die — it migrates.**
A field-count rubric scores the answer's *shape*. The model writes a shape that passes. You tighten the rubric; the defect hops to the prompt/output layer (now the answer-shape passes too). Only verification *outside* the model loop — checking the actual external object — kills it. We saw this strictly twice and across the prompt-gate family three more times. **The fix is not a smarter model. It is a smarter verifier.** The paper formalizes this as **ceiling-pin layer migration** (Definitions 1–3, §5).

> "Score the external object, not the model output."
> — the one-line repair that closes the failure mode.

**3. The corpus you delete is the corpus that would have saved the next campaign.**
We attacked our own program contract 156 times before publishing — pre-implementation, pre-commit, post-commit — and saved every rejected route. **Adversarial review is not paranoia. It is the only protocol that survives contact with a real market.**

### A few bold takes

- If your LLM trading system has not been peer-attacked at the **program-contract level**, before any code ran, you do not have a system. You have a vibe.
- The frontier of retail LLM trading is **not** bigger context windows or smarter models. It is **verification that does not live in the model**.
- Most "LLM trades the market" demos hide their failures. We saved ours. **Read the failures first**; the wins will start to look like noise.
- Pre-implementation peer review is cheap (~$0.05–$2 in API spend per campaign). The cost of skipping it is one quarter of debugging the wrong target.

## Why this is publishable, not just a blog post

We attacked our own work **156 times** before publishing. Every claim points to a runnable command:

- 225 routes, fully labelled (selected / rejected / deferred / promoted) — `data/anc/alternative-routes.jsonl`
- 52 strict-parsed peer attacks — `data/anc/attack-registry.jsonl`
- 40 verbatim quote-bank rows — `data/anc/quote-bank.jsonl`
- Every numeric claim → its source artifact → its recompute command — [`docs/evidence-locator.md`](docs/evidence-locator.md)

CI re-runs the contract checks (banned-phrase guard, paragraph uniqueness ≥ 0.85, JSON schema, cross-paper SHA, AI-disclosure block) on every push.

## Read it in 30 seconds, 5 minutes, or 30 minutes

| Time you have | Open this |
|---|---|
| 30 seconds | The four-row table above |
| 5 minutes | [Abstract + §1 of `docs/main.md`](docs/main.md) |
| 30 minutes | The full 12-page manuscript: [`latex/main.pdf`](latex/main.pdf) |
| Audit a number | [`docs/evidence-locator.md`](docs/evidence-locator.md) → run the command |

## Reproduce in three commands

```bash
git clone https://github.com/Abel-ai-causality/boundaries-of-retail-prediction-market-trading.git
cd boundaries-of-retail-prediction-market-trading
bash code/eval/boundaries-of-retail-prediction-market-trading-eval.sh
# expected: 100.00 ; hard_gate_violations=[]
```

The eval is a release-contract sanity check, **not a quality judge** — it verifies shape, not substance. To audit substance, read the manuscript and run the commands in the Evidence Locator.

## Headline numbers

| Result | Value | Source |
|---|---:|---|
| Durable >$1k/month retail trading routes | **0 of 11** trading campaigns | §4–§7 |
| Cross-mechanism ceiling-pin instances | **n=2 strict, n=3 prompt-gate family** | §5, §10 |
| Smallest filled Polymarket book | **$5.34** (23.6% spread, ~$5 NO depth) | §6 |
| Math-arb mechanism saturation | 327-trade arsenal closed; **0/4365 violations** | §4 |
| Anchor-induced LLM prior drift (sister artifact) | **256.73 probability bps** | §7 |
| R0 program-gate defects caught pre-launch (Path C) | 18 → 3 → 1 → **0** | §8 |
| R0 program-gate defects caught pre-launch (Manuscript) | 21 → 6 → 4 → 3 → **1** | §8 |
| Capacity verified shadow-only (pm-10k50k-profit, 4 candidates) | **$85,446.78** cumulative-to-50bps | §6 |

## What's in the box

```
docs/
  main.md                     the manuscript (Markdown, 585 lines)
  evidence-locator.md         every numeric claim ↔ source artifact + recompute command
  references.bib              12 cited references
latex/
  main.pdf                    compiled NeurIPS-style PDF (12 pages)
  main.tex                    Overleaf-ready LaTeX
  figures/                    6 figures (PDF vector + PNG raster)
data/
  cross-campaign-aggregate.json   17-row corpus card
  per-campaign-summary.csv        17-row campaign table
  anc/
    alternative-routes.jsonl  225 route decisions, fully labelled
    attack-registry.jsonl     52 strict-parsed peer attacks
    quote-bank.jsonl          40 verbatim quotes (per-campaign cap 8)
    methodology-self-attacks.jsonl   21 manuscript-construction objections
code/
  eval/                       single-shell readiness check (stdlib only)
  figures/                    matplotlib script regenerating figs 1, 2, 5
  extraction/                 engineering primitives from a terminated campaign
```

## Corpus card

| Layer | Count | Status |
|---|---:|---|
| Raw campaign directories | 17 | 4 sparse legacy retained for inventory honesty |
| Active campaigns analyzed | 13 | 12 full state JSON + peer artifacts; 1 peer-files-only |
| Instrumented rounds (active) | 156 | 97 infrastructure / 59 trading-focused |
| Trading-focused campaigns | 11 | Mechanism partition in `data/anc/methodology-timeline.md` |
| Recovered route decisions | 225 | 45 selected / 135 rejected / 45 deferred |
| Promoted routes (`promoted_to_next_round`) | 79 | Carried-forward into next round's candidate pool |
| Strict-parsed peer attacks | 52 | After noisy earlier parse quarantined |
| Methodology self-attacks | 21 | Manuscript-construction objections (separated) |
| Verbatim quote-bank rows | 40 | Per-campaign cap 8; peer-role cap 60% |
| Inline references | 12 | 4 arXiv + 8 journal; engaged in body, not just listed |

## What this repo is — and isn't

**Is.** A failure-preserving record of one lab's adversarial program against retail LLM-assisted prediction-market trading: the manuscript, the corpus, the attacks, the rejected routes, and the protocol that produced them.

**Is not.** A trading bot. Not financial advice. Not a recommendation to trade on Polymarket, Kalshi, or any venue. Not a claim of universal market efficiency or universal LLM trading impossibility. Bounded result: single lab, single period, suggestive — not universal. The included extraction code is engineering reference from a deliberately terminated campaign, not a working desk.

## How we got here (the protocol)

Two engineering ideas underwrote everything:

1. **R0 program gate.** Before any implementation round, the program contract is itself peer-attacked: scope drift, hidden assumptions, definition elasticity, authority-by-citation. Path C: 18 → 3 → 1 → 0 defects. Manuscript: 21 → 6 → 4 → 3 → 1. Pre-launch ambiguity made countable, not vibes.
2. **Always-on adversary.** Every implementation round writes a peer-attack file *before* the commit gate. We saved 225 rejected routes and 52 strict-parsed attacks rather than deleting them. The failure-preserving corpus is the artifact.

This generalizes beyond trading. The R0 gate and the always-on adversary are protocols, not subject-matter expertise.

## Sister paper

[MarketAnchor v0.1.2](docs/sycophancy-benchmark-marketanchor-v0.1.2.md) measures consensus-anchor sensitivity in one stored prediction-market forecasting run.
SHA-256 `8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27`.
The 256.73-bps anchor-drift result cited in §7 is reproduced from that frozen artifact.

## Cite

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

## Related work, briefly

The paper engages 12 references inline (full list in [`docs/references.bib`](docs/references.bib)):

- **Microstructure** — Wolfers & Zitzewitz (2004), Manski (2006), Glosten & Milgrom (1985)
- **AI forecasting benchmarks** — Karger et al. (2024), Cheng et al. (2026), Schoenegger et al. (2024)
- **Anchoring / prior contamination** — Lou & Sun (2024)
- **Survivorship & backtest overfitting** — Brown et al. (1992), Bailey & López de Prado (2014)
- **Pre-registration & adversarial methodology** — Nosek et al. (2018), Munafò et al. (2017), Perez et al. (2022)

Each reference is engaged in the body of the paper, not just listed.

## License

Code under [Apache-2.0](LICENSE-CODE). Manuscript, data, prose under [CC BY 4.0](LICENSE-DOCS). Both irrevocable.

## Contributing

Reproducibility fixes, verifiable-error repairs, and scope-sharpening welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). PRs should keep the eval green and include the eval log when manuscript / data / citations / code change.

## Author

Abel AI Lab — `lab@abel.ai`

The manuscript discloses AI/tool assistance directly: Anthropic Claude for peer-challenge critique and adversarial review; OpenAI Codex CLI gpt-5.5 for repository inspection, statistical recomputation, and drafting; OpenAI ChatGPT for editorial revision. These tools are not authors.

## Changelog

**v0.2.0 (2026-05-06)** — title and structure rewrite to "Legibility Is Not Deployability"; inline-cited 12-reference bibliography; formal Definitions 1–3 + capacity equation; six-figure NeurIPS layout; supplementary Evidence Locator.
**v0.1.0 (2026-05-06)** — initial public release as "Boundaries of Retail Quantitative Trading on Prediction Markets".
Full history in [CHANGELOG.md](CHANGELOG.md).
