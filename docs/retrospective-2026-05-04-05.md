# Polymarket Strategy Exhaustion Retrospective — 2026-04-24 to 2026-05-05

**Author**: Stephen Wang
**Co-research**: Anthropic Claude (propose + cross-attack) + OpenAI Codex CLI gpt-5.5 xhigh (heavy implementation + verification)
**Period**: 2026-04-24 → 2026-05-05 (12 days, ~14 campaigns, ~12 codex-hours background, ~30+ Claude-Stephen turns)
**Goal under examination**: $5k/month on $10-100k retail bankroll via systematic Polymarket trading

## TL;DR

**Yes — at 2026-05 capacity, on a $10-100k retail bankroll, BOTH (a) basic math-arb on Polymarket AND (b) non-ML feature-based strategies AND (c) LLM-as-primary-extractor strategies fail to produce sustainable $5k/month.**

Three independent failure modes exhausted in this period:
1. **Math-arb mechanisms close**: 327-trade threshold-ladder arsenal expired 2026-05; bydate LP arb only mechanism still alive but tiny capacity (~$500-1k/mo at $10k pool).
2. **Internal features can't beat liquid PM consensus**: market price aggregates more information than any retrievable feature (validated 2026-04-24 → confirmed 2026-05).
3. **LLM-as-rubric-scored-extractor ceiling-pin defect**: structural failure mode in BOTH llm-deploy R1 (PM event-contract narrative) AND Path C R1+R2 (SEC EDGAR special-situations); tighter rubric just shifts hallucination location, doesn't eliminate.

**What survived as compounding asset**:
- MarketAnchor v0.1 sycophancy benchmark (256.73 bps, p=1.59e-05, N=75 triplets) — published 2026-05-05, ready for paper / enterprise data product / talk
- Cross-mechanism ceiling-pin finding — adds dimension to MarketAnchor v0.2

**What's still open** (not falsified yet): Path D human-led + LLM-leverage; non-LLM-bottleneck signal sources (insider transactions, options flow, satellite); research-mode pivot to enterprise data product.

## 14 mechanisms / campaigns tested

| # | Campaign / Date | Mechanism class | Outcome | Net result |
|---|----------------|-----------------|---------|-----------|
| 1 | 2026-04-24 collaborative ideation | math-arb v2 (3 mechanisms) | found, point-in-time validated | mechanism arsenal — but expires |
| 2 | 2026-04 threshold-ladder alpha | math-arb-class (327-trade arsenal) | live-traded; **CLOSED 2026-05** | edge decays as participants saturate |
| 3 | 2026-04 ladder-arb (tennis O/U + crypto threshold) | math-arb-class | live but capacity tiny | $50-200/cycle ceiling |
| 4 | 2026-05-02 pm-live-readiness | paper-trading infrastructure | infra ✓ | enables others; not strategy |
| 5 | 2026-05-03 cron-fill-grounded-truth | reconcile invariants | $0 directly; engineering hygiene | required for other paths |
| 6 | 2026-05-03 ws-cron-alignment | timing infra | engineering | required infra |
| 7 | 2026-05-03 cross-platform-pilot-b | cross-venue arb (PM × Kalshi) | $0-100/cycle observed | capacity ceiling |
| 8 | 2026-05-03 profit-search | discovery / new mechanism scan | null — no new mechanisms found | exhaustion signal |
| 9 | 2026-05-03 crypto-pm-cross-venue-probe | fair-value model + cross-venue | round-0 fix landed; rolling-24h median metric defined | partial — capacity validated as ~$400/cycle ceiling |
| 10 | 2026-05-04 bankruptcy-operator | bankruptcy-claims (Cherokee Hybrid 153/158 face) | 4 estates, all mature (trade above face) | null for retail entry |
| 11 | 2026-05-04 llm-narrative-trade | LLM-prior vs market quote on event contracts | early scout | superseded by llm-deploy |
| 12 | 2026-05-04 pm-5k10k-profit + pm-10k50k-profit | capacity-tiered profit search | retail-no-mans-land confirmed | $100k retail ceiling math validated |
| 13 | 2026-05-04 llm-deploy-10k | LLM-narrative + rule-reader gate | **TERMINATED 2026-05-05** (peer convergence terminate-no-route; backtest hit_rate 41.2%, realized -23% on $4250 / 18 events) | rubric ceiling-pin (V3) + D4 borrowed-credit + 200bps edge floor < sycophancy bias |
| 14 | 2026-05-05 path-c-1week-probe | LLM-extract SEC special-situations | **TERMINATED 2026-05-05 R2** (peer probability assessment <25% no fix / 35-45% with fix) | rubric ceiling-pin moved to prompt layer; LLM hallucinates evidence |
| ★ | 2026-05-04 sycophancy-benchmark | bias quantification (research) | **PUBLISHED** (256.73 bps, p=1.59e-05, N=75 triplets) | Compounding asset; 383L research report at `docs/research/sycophancy-benchmark-marketanchor-v0.1.md` |

## Why basic math-arb on PM doesn't reach $5k/mo

### 1. Edge decays as participants saturate

Threshold-ladder alpha was the most validated math-arb mechanism (327-trade arsenal, 2026-04). Per memory `feedback_polymarket_threshold_ladder_alpha_closed_2026_05.md`: edge collapsed within 4 weeks of public discussion. PM is liquid + competitive; anyone with the same retrievable data finds the same edge; market re-prices.

### 2. Capacity ceiling at $100k retail

Retail no-mans-land pattern (validated across crypto-pm-probe, bankruptcy, llm-narrative pre-PnL):
- $1k pool: edge × small notional = unprofitable after fees
- $100k retail: too small for institutional capacity (most arb opportunities clear at $10k/cycle = 10% utilization)
- $1M+ institutional: different game (HFT, market-making, principal book)

The $5-100k retail tier is structurally caught between fee floor and capacity ceiling.

### 3. Internal features can't beat liquid PM consensus

Per `feedback_internal_features_cant_beat_liquid_pm.md`: any feature retrievable to a retail trader (price history, order book depth, PM-resolved facts) is ALSO retrievable to dozens of other retail + small-fund traders, who feed it into the consensus quote. The market price IS the aggregated forecast. Without information advantage (insider, paid-private-feed, novel data source), no internal-feature strategy can outperform the consensus on a risk-adjusted basis.

### 4. MM falsified

Per `feedback_mm_falsified_lp_arb_alive.md`: passive market-making on PM falsified at $10k pool depth — adverse selection from informed traders > spread capture. Only bydate LP arb (passive providing liquidity around resolution-date concentration) shows positive expectancy, and capacity is sub-$1k/mo.

### 5. The 327-trade backtest window confounds

Per `feedback_2026q1_test_window_too_small.md`: 3-month backtest (Q1 2026) pre-2026 train + post-2026 test hit a regime shift. Strategies that worked Q1 broke Q2-onward. Ergo any "validated" math-arb has a high regime-shift risk; the $1500/mo target must amortize against periodic breakdown.

## Why LLM-leverage strategies hit a structural ceiling

### Cross-mechanism finding (today's discovery)

Both llm-deploy AND Path C — different mechanism classes, different domains, different prompts — terminated on the SAME defect:

**Pattern**: rubric-scored LLM extraction has a structural ceiling-pin failure mode. Whether the rubric scores PM event metadata (llm-deploy 4-axis) OR SEC filing extraction (Path C 5-axis), the LLM optimizes to satisfy the rubric — including by hallucinating fields. Tightening the rubric SHIFTS where hallucination lives (rubric layer → prompt layer); doesn't eliminate.

| Layer of ceiling-pin | Example | Fix attempted | Outcome |
|----------------------|---------|---------------|---------|
| Rubric (R1-llm-deploy) | All PM gamma events surface 4 fields → confidence=100 always | terminate | strategy killed |
| Rubric (R1-Path C) | scoring.py accepts any non-empty string for axes | tighten to allowlist (R2) | layer moves |
| Prompt (R2-Path C) | LLM hallucinates allowlisted phrases (Diana/Genco: 3/7 fields fabricated) | filing-evidence gate (proposed R3) | NOT IMPLEMENTED — Stephen-side EV math killed it |

**Root cause**: post-RLHF LLMs reward confident complete answers. Rubric scoring punishes incompleteness → LLM fills missing fields with plausible fabrications. Without filing-evidence grounding gate (verbatim grep hit per scored field), the architecture is fundamentally unreliable.

### Why this kills the LLM-direct strategies

- `llm-narrative-trade`: 200bps edge floor < 256.73bps sycophancy-bias floor (from MarketAnchor v0.1) → no edge above noise.
- `Path C SEC extraction`: 0/18 quality-adjusted ≥80 confidence rate after fabrication detection → can't reach 5-candidate threshold.
- `Cross-venue LLM arb`: would inherit same prompt-layer defect.

The fix exists (filing-evidence grounding gate) but: (a) 3x API cost; (b) LLM may hallucinate grep-able quotes; (c) chunking/indexing non-trivial; (d) peer-B's probability assessment caps at 35-45% probe success even WITH fix. Not worth pursuing on $10k pool.

## What survived as compounding assets

### 1. MarketAnchor v0.1 sycophancy benchmark (PUBLISHED)

`docs/research/sycophancy-benchmark-marketanchor-v0.1.md` (383L, 9 sections, CC BY 4.0):
- N=75 complete triplets × 8 contracts × codex/gpt-5.5
- mean sycophancy effect: **256.73 bps**
- 95% bootstrap CI: **[149.80, 367.17] bps**
- t(74) = 4.62, **p = 1.59e-05**
- Asymmetric effect: ANCHORED-HIGH pulls prior up more than ANCHORED-LOW pulls down
- 9 limitations honestly listed (single LLM × single domain, claude backend bug, etc.)

**Compounding paths**:
- Academic publication (NIPS / ICML / FAccT) — credibility asset
- Enterprise data product (LLM-trading vendors need bias-correction layer) — $0-50k/yr early
- Anthropic / OpenAI consulting on bias-eval — TBD

### 2. Cross-mechanism ceiling-pin finding (NEW)

L2 memory `feedback_llm_extraction_ceiling_pin_cross_mechanism.md`:
- Rule: any "LLM extracts → rubric scores extracted fields" architecture has structural ceiling-pin defect at 2026-current model capacity
- Fix: only filing-evidence grounding gate (verbatim grep hit) reliably works
- Compounding application: MarketAnchor v0.2 should add rules-comprehension dimension with filing-evidence verification

### 3. Reusable engineering primitives

- `ws/special_situations/edgar_scanner.py` (28L stdlib RSS poller)
- `ws/special_situations/extract.py:_chunks` + `_selected` (chunk-extract + stratified sampling)
- SKIP ledger pattern (`parse_status` enum + `skip_reason_or_null`)
- CIK-collision-resistant prompt log filenames
- `ws/sycophancy_benchmark/{runner, backends, scoring, domains}.py` (UNANCHORED/ANCHORED-LOW/ANCHORED-HIGH framing harness)

### 4. abelian rule #16 round-0 gate validated

R0 program-peer-challenge gate caught 22 attacks across 4 re-gate rounds on Path C alone (v1 18 → v2 3 → v3 1 → v4 0). Saved 4h R1 burn × 4 rounds = 16h potential waste. Discipline pays.

## What's still open (not falsified)

1. **Path D — human-led + LLM-leverage**: Stephen reads filings; LLM disambiguates clauses; Stephen makes trades. NOT a programmable pipeline (defeats automation goal) but might produce $5-15k/yr genuine retail edge. Not yet tested. Cost: 5-10h/week Stephen time.
2. **Non-LLM-bottleneck signal sources**: insider transactions (Form 4 SEC + 13F), options flow (CBOE Skew Index, gamma exposure), satellite imagery (RS Metrics for retail / energy), private-data feeds (Sentieo, Quiver). These don't depend on LLM-extraction quality. NOT yet tested in this session.
3. **bydate LP arb**: alive but tiny capacity. Could compound to $500-1k/mo at $10k pool if held passively for months. Memory: `feedback_mm_falsified_lp_arb_alive.md`.
4. **Research-mode pivot**: focus MarketAnchor v0.2 expansion (claude/llama/grok backends + sports/M&A/crypto domains + filing-evidence dimension) → compounding research asset; trading P&L not the metric. Time-amortized: 6-12 months to publish + first enterprise client.
5. **MarketAnchor as enterprise data product**: sell sycophancy-bias-correction layer to existing LLM-trading vendors. Long sales cycle (6-9 months) but high LTV per client.

## Honest probability assessment for $5k/month target

| Path | $5k/mo probability | Time-to-test | Stephen-side cost |
|------|-------------------|--------------|-------------------|
| Path D human + LLM | 30-50% (untested) | 4 weeks paper | 5-10h/week |
| Non-LLM signals (insider/options/satellite) | 20-40% (untested) | 4-8 weeks per signal | varies |
| bydate LP arb scale-up | 10-15% (capacity-bounded) | 4 weeks | minimal (passive) |
| Research path (MarketAnchor v0.2) | 5-15% trading; 30-50% as enterprise pipeline | 6-12 months | 5-10h/week |
| **Continue Path C with R3 evidence-gate** | **<25% (per peer-B)** | 1 week | 4-8h + $30 codex |
| Continue PM math-arb hunt | <10% (mechanism arsenal exhausted, regime-shift risk high) | n weeks | high opportunity cost |

## Recommendation

Sequence over next 2-4 weeks:
1. **Week 1**: pause active campaigning. Consolidate today's findings: publish MarketAnchor v0.1 (blog post + post on Twitter/X technical communities; light email outreach to 2-3 LLM-trading vendors).
2. **Week 2**: probe ONE non-LLM signal source. Recommendation: insider transactions (Form 4 + 13F filing scanner — NOT LLM extraction; rule-based parsing of SEC structured data). Stephen-led, ~10h. If signal real → R1 paper-trade probe.
3. **Week 3-4**: depending on Week 2 results, either deepen Path D (human-led merger arb desk with LLM as research assistant — fundamentally different from Path C's automated extraction) OR pivot to MarketAnchor v0.2 expansion as primary work.

What NOT to do:
- Don't push Path C R3 evidence-gate. EV doesn't justify; even 35-45% success rate is fragile.
- Don't restart math-arb mechanism hunt on PM. Arsenal exhausted; regime-shift risk high.
- Don't pursue $100k institutional path with $10k retail bankroll. Capacity gap is structural.

## Open questions for Stephen

1. Publish MarketAnchor v0.1 publicly OR keep private as enterprise leverage? (publication = credibility + accelerated network effects; private = data-product moat)
2. Path D human-led desk: is 5-10h/week Stephen time acceptable, or are you optimizing for AUTOMATED edge (in which case Path D is out and we go research-pivot)?
3. Is the $5k/month target firm, or would a $1-3k/month + compounding-research-asset blend acceptable?

## References

### Today's session deliverables
- `docs/research/sycophancy-benchmark-marketanchor-v0.1.md` — 383L published research artifact
- `docs/research/2026-05-04-05-pm-strategy-exhaustion-retrospective.md` — this file
- `abelian/runs/2026-05-04-llm-deploy-10k/COMPOUND_DOC.md` — terminated llm-narrative campaign
- `abelian/runs/2026-05-05-path-c-1week-probe/COMPOUND_DOC.md` — terminated EDGAR extraction campaign
- `abelian/escalations.md` — append for both terminations + Fork 3 delivery

### Memory L2 files created/updated this session
- `feedback_llm_extraction_ceiling_pin_cross_mechanism.md` (NEW; cross-mechanism structural finding)

### Pre-existing memory L2 files cited
- `project_polymarket_alpha_arsenal.md`
- `project_polymarket_ladder_arb.md`
- `project_polymarket_math_arb_v2.md`
- `feedback_polymarket_threshold_ladder_alpha_closed_2026_05.md`
- `feedback_mm_falsified_lp_arb_alive.md`
- `feedback_polymarket_probe_edge_metric_is_upfront_cash.md`
- `feedback_2026q1_test_window_too_small.md`
- `feedback_internal_features_cant_beat_liquid_pm.md`
- `feedback_collaborative_ideation_finds_mechanism_alpha.md`

### Code artifacts (terminated campaigns)
- `ws/llm_deploy/{rule_reader, position_sizer, risk_gate, scanner}.py` (182 LOC; not in production)
- `ws/special_situations/{edgar_scanner, extract, scoring}.py` (156 LOC; not in production; engineering primitives reusable)
- `ws/sycophancy_benchmark/{runner, backends, scoring, domains}.py` (sycophancy benchmark harness; reusable for v0.2)
