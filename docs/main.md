# Boundaries of LLM-Assisted Quantitative Trading on Prediction Markets: A Multi-Campaign Empirical Retrospective from Abel AI Lab

Author: Stephen Wang (Abel AI Lab)
Email: lab@abel.ai
License: CC BY 4.0 (pending Abel AI Lab approval before arXiv submission; license is irrevocable per arXiv policy)
Date: 2026-05-05

## Foreword from Abel AI Lab

Abel AI Lab studies autonomous research systems when they touch real markets, real code, and
real institutional constraints rather than toy tasks. The lab's operating premise is simple:
AI systems become useful when they survive measurement, adversarial critique, and
operational accountability.

This paper maps a boundary. It is not a product launch note and not a trading signal sheet.
It records what happened when Abelian research loops repeatedly tried to turn
LLM-accessible market information into deployable prediction-market strategies.

The object of study is deliberately narrow. Stephen Wang ran the campaigns at Abel AI Lab
during 2026-Q2, with Claude and Codex used as adversarial research tools under a
human-authored program contract. The aim is open knowledge sharing on LLM-trading
boundaries: null results, broken gates, and capacity ceilings belong in the record.

MarketAnchor v0.1.2 is the sister paper to this retrospective. It isolates consensus-anchor
sensitivity in a stored prediction-market forecasting run and is cited here only for that
narrower construct. Its SHA256 is preserved as
8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27.

The roadmap continues from this paper. MarketAnchor v0.2 will test anchor controls more
directly, and the smart-money signal program will ask whether external participant behavior
can become a grounded signal without borrowing unsupported authority from LLM priors.

The lab does not treat LLMs as authors. Claude and Codex contributed critique, extraction,
drafting assistance, and verification pressure. The human author owns the decisions, the
claims, and the release.

The manuscript is also a lab-process artifact. It puts the empirical trading boundary and
the methodology boundary in one place, for researchers, traders, and builders who do not
want to spend weeks rediscovering the same constraints.

The standard for this draft is goal-driven evidence rather than eval-gaming. Every retained
claim advances the mechanism map, marks a limitation, or preserves provenance for reviewers
who want to attack the record directly.

The contribution is a first systematic empirical retrospective, not a universal theorem.
The evidence is single-lab and single-period, but unusually dense in adversarial review
artifacts. Abel AI Lab releases this draft to keep those artifacts legible.

## AI and Tool Assistance Disclosure

Anthropic Claude was used for peer-challenge critique, framing review, and cross-attack peer
policy in adversarial review rounds. OpenAI Codex CLI gpt-5.5, reasoning effort xhigh, was
used for repository inspection, statistical recomputation support, deep transcript mining
across peer files, data-quality repair, verified arXiv reference checks, and section
drafting assistance. The human author reviewed all outputs and accepts responsibility for
the manuscript, statistics, code references, citations, and claims.
These tools are not authors.

## Abstract
When a single research lab tries to turn LLM-accessible market information into deployable
retail trading on prediction markets, where do the routes fail? This retrospective answers
from the evidence of 13 active campaigns and 156 instrumented rounds across 12 calendar days
at Abel AI Lab in 2026-Q2. The corpus combines 12 fully instrumented Abelian campaigns, one
peer-files-only active campaign, and four sparse legacy inventories retained for denominator
honesty but excluded from active analysis. State files, peer attacks, route registries,
quote-bank evidence, and program-gate timelines are mined to map four mechanisms:
math-arbitrage
saturation, cross-mechanism LLM-extraction ceiling-pin behavior, retail-bankroll capacity
ceilings, and anchoring uncertainty as a trading constraint. The ceiling-pin pattern is
reported as n=3 observed instances, llm-narrative-trade-0125, llm-deploy-10k, and
path-c-1week-probe, with the count treated as cross-mechanism but still single-lab,
single-period, and suggestive rather than structural. The sister MarketAnchor v0.1.2 result
contributes only the narrower observation that consensus-anchor sensitivity exists in one
stored LLM forecasting run, with mean net signed drift of 256.73 probability bps; it is not
cited as tradable edge, return, or calibration error. Paper 2 separately argues that small
LLM-prior edges are not operationally independent until this anchoring uncertainty is
controlled. The methodology contribution is the empirical record of Abelian rule #16 R0
gates: Path C narrowed 18 to 3 to 1 to 0 attacks, while Paper 2 narrowed 21 to 6 to 4 to 3
to 1 before R1 extraction. The repository and Zenodo DOI are planned for public release
after Abel AI Lab license confirmation. MarketAnchor v0.1.2 remains citation pending
verification until an external identifier exists.

## 1. Introduction

This paper is the first systematic empirical map of a narrow but economically important
question: what happens when modern LLM agents are repeatedly aimed at retail-scale
prediction-market trading under adversarial review?

The question matters because prediction markets expose public prices, open settlement rules,
and fragmented liquidity in a form that looks unusually accessible to language models. A
model can read a market title, a rule page, a news article, an order book snapshot, and a
prior campaign memo inside one working context.

That accessibility creates an obvious temptation. If an LLM can summarize rules, surface
event evidence, and propose trades faster than a human retail operator, then perhaps the
remaining problem is just engineering throughput.

The campaigns studied here tested that temptation in practice. They looked for
threshold-ladder arithmetic, duplicated-market relationships, date-ladder monotonicity,
cross-platform price gaps, internal-feature residuals, LLM narrative priors, event-contract
rule extraction, and SEC special-situation extraction.

The result is not a single failure. It is a pattern of boundary conditions. Some mechanisms
die because public markets already absorbed them. Some die because the book is too thin.
Some die because the LLM can fill a rubric without grounding the field. Some die because the
measured prior is not independent of the prompt-visible consensus.

Null results matter in this domain because trading literature is prone to survivorship bias.
Failed mechanisms disappear from public memory, while backtests that once worked remain
named and reusable long after the live market changed.

The Abelian corpus is useful because it preserves the failure trail. Peer files record
objections before the operator can round them away. Mission threads preserve rejected routes
as data. Eval logs separate score movement from profit movement. Program gates show when a
research plan was too vague to launch.

The paper therefore treats the archive as an empirical object. The unit is not only a trade
or a backtest row. It is a round in which an LLM-assisted system proposed a route, mutated
code or prose, received adversarial critique, and either moved a metric or exposed a
blocker.

The active corpus is 13 campaigns and 156 instrumented rounds. The raw inventory is 17
campaigns and 164 round directories, but four legacy directories contain no transcript files
and are retained only for inventory completeness.

The analyzed period is a 12-calendar-day window ending on 2026-05-05, with active
instrumented campaign work concentrated in four active days from 2026-05-02 through
2026-05-05. This distinction matters because calendar span and active execution span are not
the same measure.

The trading subset is smaller than the corpus headline. Core infrastructure accounts for 97
rounds from pm-live-readiness and ws-cron-alignment. Cron-fill-grounded-truth adds 5
adjacent infrastructure rounds and is counted in the trading-focused remainder only when its
evidence directly bears on mechanism saturation.

The paper uses 59 trading-focused rounds across 11 active trading campaigns for the
substantive findings. Infrastructure rounds contribute to methodology and to
safety/freshness constraints, not as direct evidence of profitable trading mechanisms.

The four findings are intentionally framed as observed boundaries. Math-arbitrage saturation
describes mechanisms that were valid historically or locally but closed under current
Polymarket conditions. The LLM-extraction ceiling-pin describes confidence or rubric systems
that reach high scores without adding tradeable truth. The capacity ceiling describes the
economics of small books and fee floors. Anchoring uncertainty describes how prompt-visible
consensus contaminates claimed independent priors.

The paper does not claim that prediction markets are efficient in every niche. It reports
that in this lab's 2026-Q2 campaigns, the obvious LLM-accessible retail routes did not
produce durable greater-than-$1k-per-month edge after adversarial review.

The scope is also not a complete taxonomy of quantitative trading. The campaigns are
Stephen-curated, the operator is one person, and the tooling stack reflects Abel AI Lab's
preferences. Those limitations make the map descriptive rather than universal.

The value of the map is still practical. A builder considering a similar path can inspect
which ideas failed for data-quality reasons, which failed for economics, which failed for
LLM grounding, and which remain plausible only after new controls.

The paper structure follows the empirical path. Section 2 situates the work against LLM
forecasting, financial LLMs, prediction-market studies, and anchoring literature. Section 3
defines the corpus and methodology. Sections 4 through 7 present the four findings. Section
8 extracts the Abelian methodology contribution.

Discussion, limitations, and open problems are treated as part of the empirical result, not
as back matter. They state where the evidence stops, which mechanisms remain plausible, and
which follow-on programs would actually test the next claim.

## 2. Related Work

The nearest literature already knows how to ask LLMs for forecasts; this paper asks what
breaks when those forecasts become candidate trades. ForecastBench (arXiv:2409.19839)
builds a dynamic benchmark for open-domain AI forecasting, so it is directly relevant to
whether a model can emit useful probabilities about unresolved events. Prophet Arena
(arXiv:2510.17638) asks a related predictive-intelligence question and uses
prediction-market performance as part of the comparison surface. AI-Augmented Predictions
(arXiv:2402.07862) studies LLMs as forecasting assistants for humans rather than autonomous
capital-allocation systems. LiveTradeBench (arXiv:2511.03628) moves closer to trading by
using live market data, while Pratt et al.'s forecasting-strategy study (arXiv:2406.04446)
tests whether language models can apply named forecasting heuristics rather than merely
produce fluent rationales.

That forecasting strand contributes benchmark design, task construction, probability
elicitation, and evidence that LLMs can sometimes help forecasters. It does not by itself
answer what happens when a probability becomes a route to order placement. Other temporal
forecasting work expands the benchmark context: temporal-event evaluation
(arXiv:2407.11638), time-series prompting through AutoTimes (arXiv:2402.02370),
PROPHET-style future forecasting (arXiv:2504.01509), multimodal event forecasting
(arXiv:2408.04388), and macroeconomic forecasting with LLMs (arXiv:2407.00890) all widen
the set of domains in which forecast quality can be measured. Paper 2 is not a forecasting
benchmark. It studies what happens when LLM forecasters are treated as trading routes under
adversarial review, where the failure mode includes ceiling-pin defects in field extraction,
source grounding, and capacity, not only forecast inaccuracy.

The anchoring literature intersects forecasting at the point where a probability is no
longer merely an answer, but a response to visible context. Lou and Sun (arXiv:2412.06593)
directly study anchoring bias in large language models. SynAnchors (arXiv:2505.15392)
pushes further into mechanism and mitigation by constructing synthetic data to isolate the
anchoring effect. Sharma et al. (arXiv:2310.13548) frame sycophancy as agreement with user
beliefs or prompt pressure, and Wei et al. (arXiv:2308.03958) show that synthetic data can
reduce such behavior. Perez et al.'s model-written evaluation work (arXiv:2212.09251), the
InstructGPT RLHF paradigm (arXiv:2203.02155), Constitutional AI (arXiv:2212.08073), and
calibration-oriented language-model behavior work (arXiv:2207.05221) give the broader
alignment-era context in which assistant models are trained to be helpful, preference-aware,
and sometimes overly compliant.

Paper 2 uses that literature narrowly. It does not make a general model-behavior claim about
all LLM anchoring or sycophancy. Section 7 invokes the sister MarketAnchor v0.1.2 result only
for consensus-anchor sensitivity in one stored prediction-market forecasting run: 256.73
probability basis points of mean net signed drift. That statistic is not tradable edge, not
return, not calibration error, not forecast accuracy, and not trading profit. Paper 2's
separate trading-operational claim is that any LLM-prior trading edge below roughly 500 bps
is contaminated unless anchor controls are applied when the prior was elicited near market
consensus. The contribution is a trading-system hygiene rule, not a new taxonomy of model
psychology.

Financial-LLM work supplies the agent and domain-specialization backdrop, but not the
retail prediction-market boundary by itself. BloombergGPT (arXiv:2303.17564) shows the
value of finance-tuned language modeling at scale. FinGPT (arXiv:2306.06031) and the
related data-democratization work (arXiv:2307.10485) make the case for open finance LLM
infrastructure. FinTral (arXiv:2402.10986) extends finance LLMs into multimodal settings.
FinLLM-B (arXiv:2402.07536) evaluates LLMs for breakout trading. StockAgent
(arXiv:2407.18957), TradingAgents (arXiv:2412.20138), and market-simulation work on LLM
trading agents (arXiv:2504.10789) study agent behavior in financial decision loops.

That strand contributes model specialization, agent architecture, market-simulation
protocols, and the claim that LLMs can participate in financial workflows. Paper 2
complements it with a narrower negative map: on prediction markets specifically, at retail
bankroll scale, the obvious LLM-accessible routes in this Abel AI Lab corpus did not produce
a sustainable greater-than-$1k-per-month edge after adversarial review. The diagnosis is not
that finance LLMs are useless. It is that public market information, rule text, and prompt
priors can be easy for many participants to access, while the remaining edge is eroded by
source-grounding, fee, fillability, and capacity gates.

That positive finance-LLM backdrop needs the older financial-ML critique beside it. Lo
(2002) shows that a reported Sharpe ratio is a statistic with distributional and
serial-correlation assumptions, not a standalone proof of edge. Bailey and Lopez de Prado
(2014) formalize the deflated Sharpe ratio to correct for selection bias, non-normality, and
multiple trials. Lopez de Prado (2018, Chs. 11-12) turns that critique into workflow
guidance: backtests are research artifacts vulnerable to overfitting unless the validation
design accounts for the search process. Paper 2 imports that caution at the route level: an
LLM-generated idea is not promoted because the local score rose; it is promoted only if the
source, time, fill, and capacity gates survive.

Prediction-market-specific work brings the evaluation surface closest to the campaigns
studied here. The canonical social-science base predates the current LLM benchmark wave:
Wolfers and Zitzewitz (2004) survey prediction markets as information-aggregation
mechanisms, Manski (2006) warns that market prices do not mechanically identify a mean
belief without assumptions about preferences and wealth, and Snowberg and Wolfers (2010)
show that favorite-longshot bias can distort the interpretation of market-implied
probabilities. Those references matter here because Paper 2 treats prices as execution
constraints and consensus anchors, not as ground truth.

The newer prediction-market LLM work then supplies the direct comparison set. PolyBench
(arXiv:2604.14199) proposes a Polymarket benchmark for LLM forecasting and trading
capabilities on live prediction-market data. LiveTradeBench (arXiv:2511.03628) is adjacent
because it also treats market data as an evaluation substrate. PolySwarm (arXiv:2604.03888)
studies multi-agent prediction-market trading and latency arbitrage, focusing on emergent
behaviors when multiple LLM agents interact with the same order book. Paper 2 differs in
three ways: (a) single-operator retail bankroll rather than multi-agent simulation; (b)
failure-preserving retrospective rather than benchmark scoring; and (c) a cross-mechanism
ceiling-pin diagnosis spanning LLM-extraction failure modes that PolySwarm's
interaction-focused frame does not directly probe. Polymarket order-book microstructure
evidence (arXiv:2604.24366), 2024 election-market anatomy (arXiv:2603.03136),
prediction-market arbitrage structure (arXiv:2508.03474), and UMA-resolved Polymarket
dispute arbitration (arXiv:2604.15674) define the market context in which this paper's
campaigns operated.

Classic market microstructure explains why that market context cannot be reduced to a
probability table. Glosten and Milgrom (1985) give the adverse-selection account of bid,
ask, and transaction prices when informed and uninformed traders meet through a specialist.
Easley, Kiefer, O'Hara, and Paperman (1996) connect liquidity and information to
infrequently traded securities, a close conceptual match to thin prediction-market books.
Stoll (1989) decomposes the bid-ask spread into inventory, order-processing, and
adverse-information components. Section 6 uses those ideas operationally: a quoted edge is
not a deployable edge unless the spread, depth, inventory risk, and information asymmetry
leave enough capacity after fees.

Those papers are useful context, but the object differs. Paper 2 is not a benchmark proposal
and does not score models on a public leaderboard. It uses prediction-market campaigns as an
empirical retrospective object. The evidence comes from internal Abelian campaign logs,
state files, peer attacks, quote banks, and route registries. PolyBench and LiveTradeBench
matter because they show that the subfield is converging on live prediction-market data as a
serious evaluation ground. Paper 2 contributes the complementary artifact: a
failure-preserving map of what happened when one lab tried to turn that data into retail
trading operations.

Survivorship bias and false-positive control supply the final lens because trading failures
usually vanish before they become evidence. Brown, Goetzmann, Ibbotson, and Ross (1992)
show how performance studies can be distorted when failed funds disappear from the sample.
Harvey, Liu, and Zhu (2016) make the factor-zoo problem explicit: once enough candidate
signals are tried, conventional thresholds are no longer credible evidence of expected
return. Bailey and Lopez de Prado (2014) add the deflated Sharpe ratio as a correction for
selection, backtest overfitting, and non-normal returns, while Lo (2002) shows why Sharpe
ratio inference itself depends on the return process. Lopez de Prado (2018, Ch. 11)
concentrates the warning in financial-machine-learning terms: even a flawless-looking
backtest can be wrong if it is a product of the search procedure.

Paper 2 does not try to settle that literature. It uses the warning operationally: failed
campaigns are preserved as data, not omitted as embarrassing dead ends. The relevant unit is
not only a profitable row; it is the route that was proposed, attacked, narrowed, rejected,
or quarantined before money could scale. That design is intentionally hostile to
survivorship. The 4 sparse legacy inventories remain in the denominator, the 13 active
campaigns are separated from the 17 raw directories, the R2 eval-gaming failure is preserved
as a methodology lesson, and promoted routes are reported beside rejected and deferred
routes.

That operational use is methodologically important for the LLM-trading subfield. Most agent
papers naturally emphasize successful trajectories, benchmark scores, or simulations that
finish with a model-comparison table. This paper keeps R0 refusals, peer attacks, route
rejections, ceiling-pin failures, and eval-gaming repairs in the empirical record. The null
result is therefore not a blank outcome. It is a structured account of which routes failed
at which gate, with the same archive also preserving the few routes that remained plausible
only after tighter controls.

Across the five strands, the distinct contribution is therefore specific. Paper 2 does not
claim a universal limit on prediction-market efficiency, a universal limit on LLM trading,
or a new general theory of anchoring. It contributes the first Abel AI Lab multi-campaign
retrospective of LLM-assisted retail prediction-market trading attempts: 13 active
campaigns, 156 instrumented rounds, explicit corpus exclusions, source-grounding evidence,
capacity analysis, anchor-control implications, and an Abelian methodology record that keeps
failed routes available for audit.

| Paper or benchmark | Substrate | Object of study | Failure preservation | Methodology contribution | Lab structure | Quantitative outcome |
| --- | --- | --- | --- | --- | --- | --- |
| Paper 2 | Abel AI Lab campaign archive plus Polymarket/Kalshi-adjacent route evidence. | Retail LLM-assisted prediction-market trading attempts under adversarial review. | High: R0 refusals, rejected routes, ceiling-pins, and eval-gaming repairs remain in the corpus. | Failure-preserving retrospective with route gates for sourceability, fillability, capacity, and anchoring. | Single-lab, single-operator, single-period. | 13 active campaigns, 156 instrumented rounds, n=3 ceiling-pin observations, and no durable greater-than-$1k-per-month route. |
| PolyBench (arXiv:2604.14199) | Live Polymarket data packaged as an LLM benchmark substrate. | LLM forecasting and trading capability on prediction-market tasks. | Benchmark-oriented: failures appear through model scores rather than preserved campaign archaeology. | Public task construction for live prediction-market evaluation. | Benchmark paper, not this lab's retrospective corpus. | Quantitative outcome is model-performance benchmarking, not a single-operator PnL boundary. |
| LiveTradeBench (arXiv:2511.03628) | Live market data for real-world alpha-seeking evaluation. | Whether LLM agents can seek trading alpha in live settings. | Partial: failed predictions can be scored, but the paper is not built around retained route refusals. | Moves evaluation from static finance QA toward live trading substrates. | External benchmark setting rather than Abel AI Lab's single-operator archive. | Quantitative outcome is benchmark performance, not failure-preserved route attrition. |
| Prophet Arena (arXiv:2510.17638) | Prediction-market-linked forecasting arena. | Predictive intelligence of LLMs across unresolved events. | Low-to-medium: the emphasis is arena comparison, not rejected-trade provenance. | Treats prediction-market performance as an evaluation signal for forecasting intelligence. | Multi-model arena framing, not a single-lab trading campaign. | Quantitative outcome is arena/model comparison, not deployable capacity or after-fee execution. |

## 3. Empirical Setting and Methodology

The evidence base is small by lab count and unusually dense by audit trail. The Abelian run
registry yields 13 active campaigns and 156 instrumented rounds. The raw inventory contains
17 campaigns and 164 round directories, but four sparse legacy campaigns contain empty round
directories and are excluded from active analysis.

The active campaign set consists of 12 fully instrumented campaigns with state files plus
peer artifacts and one peer-files-only active campaign. The instrumentation enum in
cross-campaign-aggregate.json is restricted to full_state_json, peer_files_only, and
empty_legacy, which keeps a thin legacy directory from masquerading as a campaign with
round-level evidence.

The active execution span is four active days inside a 12-calendar-day window. The earliest
active campaign directory is 2026-05-02, and the final R1/R2 paper artifacts are dated
2026-05-05 and 2026-05-06.

Infrastructure dominates the round count, so the paper separates operational hardening from
trading evidence before drawing mechanism claims. Core infrastructure accounts for 97 of
156 instrumented rounds: pm-live-readiness contributes 57 rounds and ws-cron-alignment
contributes 40 rounds. Cron-fill-grounded-truth contributes 5 adjacent infrastructure rounds
and is discussed separately when it bears on mechanism evidence.

The trading-focused empirical record is therefore 59 rounds across 11 active trading
campaigns. This paper uses that partition to avoid treating infrastructure hardening as
direct trading evidence.

R2 repaired the R1 attack registry because a noisy failure archive is only a different kind
of false precision. The old heuristic registry had 3,719 rows and counted transcript noise,
route bullets, pass lines, and raw Codex diffs. The repaired registry admits only formal
attack blocks with explicit nearby severity and line spans.

Paper 2 self-attacks are quarantined into methodology-self-attacks.jsonl. They remain useful
evidence for the methodology contribution but no longer enter cross-campaign recurrence
counts.

R2 also rebuilt the quote bank so every quote appears verbatim in its cited source file at
its stated line range. The bank is capped by campaign and peer role, preventing one dense
infrastructure campaign from dominating the manuscript's textual evidence.

Alternative routes are now split into est_metric_delta_value and est_metric_delta_raw.
Numeric estimates are floats only when the source row gave an explicit numeric value;
qualitative strings remain raw text with source-file and source-line provenance.

The methodology timeline records the first observed R0 program gate at 2026-05-04T01:01:07Z
and separates retrospective campaigns from later pre-launch program-gated campaigns.

The provenance boundary is explicit. It states what the paper uses as trading evidence, what
it uses as methodology evidence, and what it quarantines as self-review.

A route is treated as live only after the evidence chain reaches sourceability,
fillability, capacity, and post-fee economics. A language model can accelerate the search
through that chain, but it does not remove any link from the chain.

### 3.1 Routes Considered Map

The alternative-route corpus is where the retrospective stops being a winner's diary.
It records paths the agents considered and did not take. The aggregate campaign table counts
228 proposed alternative routes across 156 instrumented rounds. The recovered JSONL registry
contains 225 individual route rows: 45 selected, 135 rejected, and 45 deferred. The rejection
rate is therefore 59.2% using the aggregate denominator and 60.0% using recovered registry
rows.

Promotion is also informative because it shows what the loop found worth carrying forward,
not only what it killed. The aggregate table counts 82 routes promoted to subsequent rounds;
the recovered route registry contains 79 promoted rows. Keyword coding of those 79 promoted
rows shows 10 evidence, source, filing, or grounding routes; 16 prior, quote, anchor,
ablation, or consensus routes; and 39 capacity, backtest, depth, fill, fee, spread,
settlement, or PnL routes. Those categories match the four empirical findings rather than
forming a separate appendix-only story.

The most frequently repeated route IDs were not hidden alpha routes. They were process and
infrastructure routes: `baseline-only` appeared in cron-fill-grounded-truth and
ws-cron-alignment, `skip-baseline` appeared in the same two campaigns and was rejected
because it violated verify-before-mutate, and `both-tracks-parallel`, `lp-rigor-track`, and
`all-three` each appeared twice inside ws-cron-alignment. The repeated lesson was almost
mundane: measurement discipline and websocket/LP rigor kept resurfacing because the system
could not safely reason about edge until the measurement substrate held still.

The highest numeric rejected estimates in state mission threads make the same point in a
sharper form. `cron-flagged-plus-shard-rotation` estimated +100 but was rejected because it
required new sharding logic rather than the cheaper verifier route
(`2026-05-03-0245-ws-cron-alignment/state.json:L89-L104`). `multi-conn-sharding` also
estimated +100 but was deferred behind time-sharded rotation because it required lifecycle,
watchdog, and logging refactors
(`2026-05-03-0245-ws-cron-alignment/state.json:L243-L251`). `hybrid-multi-and-fast-rotation`
estimated +100 but was rejected as over-complex once multi-connection coverage alone became
the cleaner mechanism (`2026-05-03-0245-ws-cron-alignment/state.json:L447-L455`). A route
can promise maximum metric movement and still lose because its blast radius makes the next
failure harder to observe.

The route map therefore supports a path-dependency claim. Most edges were not undiscovered;
they were proposed, attacked, and either selected, rejected, deferred, or promoted with a
blocker chain. The rejected pile teaches that high nominal metric movement often lost to
implementation blast radius, observability risk, or failure to create profit evidence.

## 4. Math-Arb Mechanism Saturation

Math-arbitrage on Polymarket no longer paid at the retail scale tested here. Across the
trading-focused corpus, the most mechanical routes were repeatedly narrowed by current-data
checks, book-depth checks, settlement checks, and capacity checks.

The threshold-ladder memory gives the cleanest cautionary contrast. A prior arsenal
recorded 327 walk-forward trades over 14 months at positive per-leg returns, but the
2026-05-03 current-market query found zero violations across 4,365 live markets in the
relevant NBA, tennis, and soccer ladder families.

That contrast is the important empirical shape: a mechanism can be real historically and
closed operationally later. The paper treats the 327-trade record as point-in-time evidence,
not as forward alpha.

The market-making branch closed in a different way. The ws-cron-alignment campaign's MM
sweep tested delta settings against live fill and markout behavior. At 100 bps, 5 of 6 fills
lost money; at 200 bps, 0 of 3 were winning; at 300 bps, n=2 was too small to rescue the
route.

The peer-B synthesis in the memory file describes adverse markout as 3 to 30 times captured
spread and characterizes Polymarket flow as informed enough that vanilla maker-edge did not
survive.

The surviving Polymarket math-arb niche was bydate LP-detected ladder arbitrage. Two Trump
China visit baskets survived the R37/R38/R39 chain with concrete live feasible price
relationships, but their inside size was measured in cents to low double-digit dollars per
poll, not institutional deployment size.

Cross-platform-pilot-b added a broader capacity warning. Cross-venue routes can be
conceptually attractive, but the observed cycle economics remained bounded by venue access,
book depth, and per-cycle capital that was too small to support a $10k to $100k retail pool
target.

The internal-feature ML memory supplies the parallel market-efficiency result. On liquid
Polymarket markets, LGBM models using only market-internal price, volume, momentum, and
category features were uniformly below market p_snap AUC. The order book already
incorporated those features.

The shared mechanism is saturation, not impossibility. Public, liquid, mechanically obvious
relationships get arbed. Internal features visible to all participants do not become private
signal by passing through a model.

This is the saturation result.

The trading-focused campaign count is 11, and 8 of those explored math-arb-class or adjacent
market-structure routes. None produced a sustainable greater-than-$1k-per-month edge after
the current-data, fillability, and capacity gates were applied.

The one-row campaign summary makes the good/bad balance explicit. Cron-fill-grounded-truth
and ws-cron-alignment are infrastructure-heavy but still contribute math-arb evidence after
down-weighting (`per-campaign-summary.csv:L3-L4`). Cross-platform-pilot-b, profit-search,
pm-5k10k-profit, and pm-10k50k-profit are capacity-ceiling rows rather than pure failures
(`per-campaign-summary.csv:L5-L6,L10-L11`). Crypto-pm-probe is the cleanest negative
math-arb row because it repeatedly closes on freshness, settlement, and capacity
(`per-campaign-summary.csv:L7`). The result is balanced: the 327-trade arsenal was real
historical alpha, bydate LP arb survived with tiny capacity, and cross-platform scans found
real but sub-floor cycle economics; vanilla market-making, internal-feature LGBM, and live
threshold-ladder violations failed current deployment checks.

The quote bank anchors the saturation claim at the places where the routes actually broke:
Q001 abelian/runs/2026-05-03-0014-cron-fill-grounded-truth/round-1/peer-B.txt:L60-L60;
Q002 abelian/runs/2026-05-03-0245-ws-cron-alignment/round-1/peer-A.txt:L39-L39; Q003
abelian/runs/2026-05-03-0245-ws-cron-alignment/round-1/peer-A.txt:L171-L171; Q004
abelian/runs/2026-05-03-0245-ws-cron-alignment/round-2/peer-B.txt:L19-L19; Q005
abelian/runs/2026-05-03-0245-ws-cron-alignment/round-2/peer-B.txt:L21-L21.

The practical implication is front-loaded verification. Math-arb work begins with
current-data violation counts, book-depth measurement, and settlement/fillability proof.
Backtest history alone is insufficient after market-maker incentives or competing bots
change the live state.

The claim is deliberately narrow. It does not say that every prediction-market arbitrage is
gone. It says the obvious Polymarket retail mechanisms in this corpus either closed, shrank
below useful capacity, or required a different external information source.

The saturation claim is strongest when the source campaign reports a live-market falsifier,
not merely a peer's preference. For this reason, ladder closure, vanilla market-making
markout, bydate LP survival, and internal-feature ML are separated rather than collapsed
into a single math-arb verdict.

## 5. Cross-Mechanism LLM-Extraction Ceiling-Pin

The most dangerous LLM trading failure in the corpus was not low confidence. It was false
high confidence. The observed ceiling-pin count in this draft is n=3: llm-deploy-10k,
path-c-1week-probe, and the in-flight llm-narrative-trade-0125 R3 observation. The claim
remains suggestive, not structural. Three instances across one lab and one period justify a
mechanism warning; they do not prove that all LLM trading systems share this defect.

We extend the program contract's initial n=2 scope to n=3 by including the in-flight
llm-narrative-trade-0125 R3 observation. This was not part of the original campaign
goal-met criterion (ii), which focused on llm-deploy and Path C. The upgrade is empirically
defensible because the narrative-trade case exercises the same failure family at the prompt
and gate layer: an LLM-derived object reaches actionability before the system has proved
source grounding, semantic alignment, realized PnL, and capacity. It is reported separately
so the reader can discount it without invalidating the cleaner n=2 extraction result.

The defect class is not "the model said something wrong." It is narrower: a rubric-layer or
prompt-layer surface lets an LLM-created field, prior, or confidence score reach the top of
the decision stack before the evidence chain reaches the source text, tradeable market, or
fillable book. In a trading system, that is more dangerous than a low score. A low score
blocks. A ceiling-pinned score routes capital toward an unverified object.

Instance one is llm-deploy-10k, the cleanest rubric-side case. The rule-reader confidence
score used four fields worth 25 points each: resolution source, deadline, fallback clauses,
and expected payoff table. For Polymarket Gamma binary closed events, those fields were easy
to populate from venue metadata. The result was a pre-trade rule gate that looked strict in
the program contract and became non-discriminative in the data.

evidence: "0/18 events were skipped on `rule_reader_confidence < 80` — every event scored 100. This is a ceiling-pinned signal" — 2026-05-04-llm-deploy-10k/round-1/peer-A.txt:L16-L16

evidence: "Rubric is `25 × n_extracted_fields` and PM gamma metadata trivially has all 4 fields" — 2026-05-04-llm-deploy-10k/round-1/peer-A.txt:L39-L39

evidence: "passed_rule_reader (≥80 confidence) | 18 (100%)" — 2026-05-04-llm-deploy-10k/COMPOUND_DOC.md:L22-L22

evidence: "18-event historical backtest shows -23% net on $4250 deployed with hit_rate 41.2%" — 2026-05-04-llm-deploy-10k/COMPOUND_DOC.md:L4-L4

The attack-row view is: CP-LD-1, severity MAJOR, source
`2026-05-04-llm-deploy-10k/round-1/peer-A.txt:L16`, states that 0 of 18 events were skipped
by the rule-reader threshold; CP-LD-2, severity MAJOR, source
`2026-05-04-llm-deploy-10k/round-1/peer-A.txt:L39`, identifies the 25-times-field-count
rubric; CP-LD-3, severity BLOCKER, source
`2026-05-04-llm-deploy-10k/COMPOUND_DOC.md:L22-L29`, ties the ceiling-pin to 18 of 18
rule-reader passes and -23.4% net return. These are cited as direct source rows because the
strict bracket-form attack parser did not ingest this peer file's narrative attack format.

The rubric layer failed because it measured field presence rather than discriminative
comprehension. A real rule-reading gate asks whether fallback clauses are ambiguous, whether
the resolution source is operationally available at settlement time, whether payoff tables
contain edge cases, and whether the market metadata is enough to reconstruct the tradeable
claim. The deployed rubric instead awarded maximum credit for fields the venue already
surfaced. It did not fail open through a coding crash; it failed closed-looking by returning
100 on every sampled event.

The trading outcome matters because it prevents the section from becoming merely a schema
critique. The same run reported 17 simulated positions from 18 scanned events and a
negative realized result. The gate did not protect the paper-trade loop from a bad strategy.
The confidence number and the PnL moved in opposite directions: the extraction layer said
all events cleared the rule-reading bar, while the backtest lost nearly a quarter of
deployed capital. That is the ceiling-pin in its pure form.

The alternative is not a fifth field worth 20 points. The alternative is a fail-closed
evidence gate. A rule-reader row carries exact source spans for the clauses that matter to
settlement and sizing. If a field is absent, ambiguous, or only inferable from generic venue
boilerplate, the system nulls the field before ranking and before position sizing.
Confidence follows source-grounded discriminators; it is not a reward for filling slots.

Instance two is Path C, the EDGAR special-situations probe. R1 repeated the llm-deploy
defect in a different mechanism: regulatory and consideration axes could auto-credit generic
strings. The domain changed from Polymarket Gamma markets to SEC filings, but the same
engineering mistake recurred. The rubric rewarded an answer-shaped field before it verified
that the field meant what the trading route needed.

evidence: "R1 ships SAME ceiling-pin defect class as llm-deploy V3 (regulatory + consideration_quant axes auto-credit on truthy-string)" — 2026-05-05-path-c-1week-probe/round-1/peer-A.txt:L8-L8

evidence: "regulatory_agency axis ceiling-pinned: `scoring.py:10-11` accepts ANY non-empty string" — 2026-05-05-path-c-1week-probe/round-1/peer-A.txt:L39-L39

evidence: "consideration_quant axis ceiling-pinned: `scoring.py:5` accepts ANY non-empty string" — 2026-05-05-path-c-1week-probe/round-1/peer-A.txt:L40-L40

R1's regulatory axis confused an SEC filing recipient with a merger-clearance authority. That
is economically load-bearing. A merger-arb route needs to know whether HSR, DOJ, FTC, CFIUS,
EU Commission, SAMR, or a comparable approval process can delay or kill a deal. "SEC" can
appear in almost every filing and does not by itself price regulatory risk. A truthy string
therefore looked like diligence while removing diligence from the path.

Path C R2 repaired the most obvious code-level auto-credit problem and then revealed the
same defect class at the prompt layer. The LLM produced plausible allowlisted phrases such
as "none required" and financing prose that passed the tighter rubric even when the cited
filing chunks did not contain those strings. The gate moved from rubric-side slot filling
to prompt-side plausible-string generation.

evidence: "the SOLE high-confidence row is a hallucination on 3 fields" — 2026-05-05-path-c-1week-probe/round-2/peer-A.txt:L8-L8

evidence: "the LLM fabricated \"none required\" in the JSON output" — 2026-05-05-path-c-1week-probe/round-2/peer-A.txt:L41-L41

evidence: "Quality-adjusted ≥80 rate = 0/18 today" — 2026-05-05-path-c-1week-probe/round-2/peer-A.txt:L63-L63

The attack-row view is: CP-PC-1, severity CRITICAL, source
`2026-05-05-path-c-1week-probe/round-1/peer-A.txt:L56-L64`, shows the regulatory axis
ceiling-pin on SEC and similar filing-recipient strings; CP-PC-2, severity CRITICAL, source
`2026-05-05-path-c-1week-probe/round-1/peer-A.txt:L65-L71`, shows the consideration axis
accepting prose rather than a numeric ratio; CP-PC-3, severity CRITICAL, source
`2026-05-05-path-c-1week-probe/round-2/peer-A.txt:L45-L63`, shows the R2 migration from
rubric auto-credit to prompt-side hallucinated allowlist strings. The same source rows also
explain why the quality-adjusted high-confidence rate fell to 0 of 18.

The Path C evidence is stronger than a single hallucination anecdote because the round
history shows layer migration. R1 had an easy scoring surface. R2 changed the surface and
the LLM still reached the top by emitting strings that satisfied the checker. The failure is
therefore not limited to one bad regex. It is a design warning: any gate that checks the
model's output rather than the filing can be passed by the model's ability to write a
credible answer.

The filing-grounded alternative is concrete. The extractor returns each trade-weighted field
with a source span, accession number, and byte or line location. The verifier greps the
filing text, not the model output. Fields absent from the filing become nulls even when the
model can infer, remember, or narrate them. Ranking uses only the post-verification row, and
backtests count rows that lose fields during grounding as non-passes rather than
low-confidence successes.

Instance three is llm-narrative-trade-0125. It is adjacent rather than identical because the
object being scored is an LLM prior, not a filing field. It still belongs in the n=3 family
because the actionability surface is prompt and gate design. The campaign repeatedly had to
separate source-grounded probability estimates from market-quote anchoring, source
decoration, nondeterminism, and semantic mismatch before any flagged row could be treated as
trade evidence.

evidence: "Engine prompt embeds market_quote BEFORE asking for prior" — 2026-05-04-0125-llm-narrative-trade/round-1/peer-A.txt:L15-L15

evidence: "the LLM is NOT citing the SOURCE BUNDLE. It's citing FACTS FROM TRAINING DATA" — 2026-05-04-0125-llm-narrative-trade/round-1/peer-A.txt:L55-L55

evidence: "Signal: **7/8 events** show with-quote prior pulled toward market regardless of sign" — 2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L24-L24

evidence: "Updated `with_quote=False` prompt to explicitly prohibit market anchoring." — 2026-05-04-0125-llm-narrative-trade/round-3/codex-implement.txt:L13015-L13015

evidence: "events_with_24h_pnl_backfilled: `0`" — 2026-05-04-0125-llm-narrative-trade/round-3/codex-implement.txt:L13047-L13047

The attack-row view is: CP-NT-1, severity MAJOR, source
`2026-05-04-0125-llm-narrative-trade/round-1/peer-A.txt:L15`, identifies market quote
exposure inside the prior prompt; CP-NT-2, severity MAJOR, source
`2026-05-04-0125-llm-narrative-trade/round-1/peer-A.txt:L55`, identifies source-decoration
rather than source-bundle citation; CP-NT-3, severity MAJOR, source
`2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L15-L24`, records 7 of 8 with-quote
priors pulled toward market; CP-NT-4, severity MAJOR, source
`2026-05-04-0125-llm-narrative-trade/round-3/codex-implement.txt:L13015-L13047`, records the
anti-anchor prompt repair and the absence of 24-hour PnL backfill at log time.

The R1 problem was not merely that the model saw the market quote. The program contract
wanted the LLM to read sources first, emit an independent prior, and only then compare to
the venue price. The implementation supplied the market quote inside the prior prompt. That
made the timestamp schema look clean while the semantic ordering was contaminated. A row can
satisfy a prior-before-quote timestamp field and still be prompt-anchored if the model saw
the quote during prior generation.

The R2 problem sharpened the mechanism. The campaign added source text, ablation, ensemble
calls, and CLOB checks. Peer review then showed that with-quote priors were pulled toward the
market on seven of eight events and that three-agent nondeterminism was large relative to
small expected edges. The model could produce a number, but the system had not yet proved
that the number was an independent, stable, source-grounded estimate.

R3 repaired part of the prompt layer by explicitly instructing the no-quote branch not to
anchor and by dropping a contradictory ablation gate. Six rows flagged under the new
criteria, but zero 24-hour PnL rows were backfilled at the time of the implementation log.
Two of the top three semantic checks were still marked unclear. That is why the observation
is included as suggestive evidence of the ceiling-pin family rather than as a completed
profit result.

The actionability alternative is the same principle with a different verifier. An LLM-prior
route makes the no-quote prior canonical, hides consensus until after prior generation,
records source publication dates, requires independent semantic agreement with market rules,
measures ensemble variance, and attaches realized exit marks before crediting a flagged row.
The output number does not become a position simply because it crosses a gate.

Together, the three cases support a disciplined claim. LLM extraction and prior-generation
systems can look most confident precisely when their scoring layer is easiest to satisfy.
The manuscript reports n=3 cross-mechanism observations, suggestive not structural. The
shared remedy is evidence grounding at the object that carries trade weight: a filing span
for an extracted field, a market-rule span for a semantic interpretation, a book snapshot
for fillability, and a realized mark for PnL.

The post-quarantine recurring-attacks file is stricter than this narrative grouping. It
retains one formal cross-campaign subclass, `schema-contract`, with 10 instances across
cron-fill-grounded-truth and ws-cron-alignment
(`anc/recurring-attacks.csv:L1-L2`). That is the surviving registry-level recurrence, while
ceiling-pin remains an n=3 source-row pattern. The distinction prevents the paper from
pretending that parser-level recurrence and mechanism-level analogy are the same evidence
class.

MarketAnchor v0.1.2 is relevant only as a separate warning that LLM forecasters can move
under consensus-anchor framing. It does not prove the ceiling-pin by itself. It explains why
independent-prior language needs controls before a prior-gap strategy is credited.

The paper's claim discipline matters. The n=3 count is not inflated with Paper 2
self-attacks and is not upgraded to a theorem. If a reviewer accepts only the cleaner
extraction cases, the evidence still supports an n=2 llm-deploy plus Path C warning. If the
reviewer accepts the prompt-gate family as the same class, the n=3 version is the more useful
engineering map.

## 6. Capacity Ceiling at Retail Bankroll

A 23.6% spread on $5.34 is not a retail trading strategy. That is the capacity ceiling in
its smallest, clearest form. The campaigns repeatedly found routes that were interesting at
small notional sizes but did not scale to the $5k to $100k retail tier without losing edge.

The ceiling is a ladder of regime changes, not a single dollar number. A $1k pool can run
smoke tests and tolerate a few tiny fills, but fixed fees, manual time, and variance dominate
the economics. A $10k pool needs repeated independent rows to avoid spending most of its
time idle. A $25k pool starts to require routing discipline because one-off $50 to $200
fills no longer move portfolio returns. A $100k pool needs many concurrent rows, deep books,
or patient resting orders. A $1M-plus pool is a different institutional, HFT, or
principal-book regime outside the evidence in this paper.

Crypto-pm-probe illustrates the small-cycle version. A route could look attractive on gross
spread, but the bottleneck side of the book carried only a few dollars of fillable size. That
is not a rounding issue. It changes the object being evaluated from a portfolio strategy to
a market microstructure curiosity.

evidence: "11 contracts at NO best price ≈ $0.485 = ~$5.34 of fillable NO depth" — 2026-05-03-2025-crypto-pm-probe/round-2/peer-A.txt:L74-L74

evidence: "AXIS 2 FAILS FILLABILITY — the alleged 23.6% spread is CAPACITY ≤ $5.34" — 2026-05-03-2025-crypto-pm-probe/round-2/peer-A.txt:L74-L74

evidence: "R3 must: (a) reject rows where min(inside_size_yes_dollars, inside_size_no_dollars) < $100" — 2026-05-03-2025-crypto-pm-probe/round-2/peer-A.txt:L75-L75

The lesson is capacity-weighted edge. A 23.6% spread on $5.34 is not comparable to a 200 bps
signal on $50k. The former can be real and still irrelevant to a retail pool that targets
greater-than-$1k-per-month profit. This is the same adverse-selection logic that standard
market microstructure applies to spread capture. Glosten and Milgrom (1985) explain why bid
and ask quotes embed the risk of informed trading; Easley, Kiefer, O'Hara, and Paperman
(1996) connect liquidity and information when trading is infrequent; Stoll (1989) separates
spread components that cannot be treated as free expected return. The displayed price is
economically meaningful only when the trader can fill enough size without moving into worse
levels or being selected against by better-informed flow. Prediction-market order-book
studies in the reference set, including arXiv:2604.24366, are useful background for that
distinction.

llm-narrative-trade-0125 exposes the pre-PnL version. Peer review found a real CLOB book for
one striking gap, but the immediately tradeable amount was still retail-small. The same
paragraph that falsified the stale-Gamma hypothesis also warned that the deployable slice was
limited without multi-day queueing or larger event selection.

evidence: "CLOB book: bid=0.51, ask=0.52, inside_size_yes=11130 USDC, inside_size_no=16052 USDC" — 2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L82-L82

evidence: "at $50-100 inside-size per fill before slippage past 0.52→0.55 = ~$200-500 deployable" — 2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L83-L83

evidence: "At $50-200 per-event inside-size and 30+ events for statistical power, daily deployable ≈ $3-6k" — 2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L88-L88

Those numbers define the $10k-to-$100k transition. At $10k, a $3k daily inflow can matter if
holding periods are short and realized edge is large. At $25k, the same inflow is already a
utilization problem unless many rows can run in parallel. At $100k, the route either scales
opportunity count by roughly an order of magnitude, keeps orders resting for many days, or
moves into larger markets where the LLM edge is less likely to survive.

Bankruptcy-operator-0125 contributes a different capacity failure: access depth rather than
book depth. The available public-scrape evidence did not expose enough claim-specific
executable inventory. Aggregate pricing pages and plan snippets can support a desk memo, but
a $100k deployer needs class, minimum size, transfer mechanics, fees, and actual broker
quotes.

evidence: "The claims_log has only two rows." — 2026-05-04-0125-bankruptcy-operator/round-1/peer-B.txt:L94-L95

evidence: "the dataset is sparse" — 2026-05-04-0125-bankruptcy-operator/round-1/peer-B.txt:L97-L98

evidence: "public web scraping does not expose enough live, actionable, claim-specific inventory for a $100k deployer" — 2026-05-04-0125-bankruptcy-operator/round-2/peer-B.txt:L25-L25

The bankruptcy route shows why capacity is not only book depth. It can also be access depth.
If the true opportunity requires broker relationships, claim-transfer paperwork, KYC,
minimum ticket sizes, and class-specific legal diligence, then a public scraper has not
reached deployable capacity even when it reaches real documents. The route may still exist
as an operator business, but it is not the same as a low-touch LLM trading system.

PM-10k50k-profit gives the most constructive counterexample. One round verified
cumulative-to-50bps capacity of $85,446.78 across four accepted candidates and treated that
capacity as a frontier artifact rather than fantasy PnL. Later peer review verified that
the frontier was shadow-only, that no live orders were created, and that deployable rows
still needed current evidence and priors before paper entry.

evidence: "accepted_capacity_usd=85446.78 across 4 accepts (~$21k avg) is plausible for PM mid-tier liquidity" — 2026-05-04-1846-pm-10k50k-profit/round-1/peer-A.txt:L35-L35

evidence: "capacity stats excluded from pool_value_delta_usd — prevents the \"phantom pool growth from unfilled candidate depth\" inflation class" — 2026-05-04-1846-pm-10k50k-profit/round-1/peer-A.txt:L36-L36

evidence: "40 rows, 8 deployable candidates, 15 capacity-deployable rows, 30 required-prior-deployable rows, 0 positions appended, 0 live orders" — 2026-05-04-1846-pm-10k50k-profit/round-20/peer-B.txt:L17-L17

This counterexample matters because it prevents the section from claiming that retail
capacity is always tiny. Some mid-tier Polymarket rows can display five-figure capacity
within a slippage band. The missing piece is simultaneous evidence: official source
routeability, fresh market data, a prior strong enough to clear the raw-prior ceiling, and a
paper execution path. Capacity alone does not become PnL, but capacity measured separately
keeps the system honest.

Cross-platform-pilot-b adds the venue-matching version of the ceiling. Cross-venue spread
ideas are attractive precisely because they appear to escape a single venue's order-book
limits. The campaign evidence instead pointed to matching failure and operational capacity
near zero for the tested route. A cross-venue mechanism proves shared event semantics, venue
access, fee models, withdrawal and settlement latency, and both-side depth before it can
claim scale.

The pool-tier map follows from those cases. Around $1k, the right question is whether the
mechanism survives a smoke test without hidden fees or obvious leakage. Around $10k, the
question becomes whether opportunity frequency prevents idle capital. Around $25k, row
independence and fill sequencing begin to matter because a few small fills cannot drive
returns. Around $100k, the route reports inside size, expected hold time, fee drag,
settlement status, and post-fee PnL in one ledger. Beyond $1M, the evidence needed is
institutional: queue priority, rebate and fee tiers, API latency, private inventory, and
principal-book risk.

The recurring peer pattern is that idea generation was rarely the binding constraint. The
binding constraint was turning an idea into fresh, fillable, settlement-grounded,
capacity-weighted deployment. A route that cannot report inside size, expected hold time,
fee drag, and settlement status is not yet a retail-bankroll route. These are blockers, not
details for later optimization.

The retail tier is therefore caught between fee floor and capacity ceiling. The most
mechanical opportunities are too small, the liquid markets are too efficient, and LLM-sourced
priors require an uncertainty buffer large enough to erase many apparent edges. Capacity and
edge have to be evaluated as one object from the first round, not after a nominal alpha has
already been declared.

Across the 11 trading-focused campaigns, at least six quantified cycle or row economics
below the intended deployment floor before claiming profit: cross-platform-pilot-b reached
0 of 30 overlap on the reference corpus and therefore $0 capacity on that target; profit
search ended at $0.32/day on a $100k pool; crypto-pm-probe exposed a $5.34 bottleneck;
llm-narrative-trade measured roughly $200 to $500 deployable on the sharpest single row and
$3k to $6k daily deployability only after 30-plus rows; bankruptcy-operator found only two
claim rows and no executable $100k inventory; pm-10k50k-profit found $85,446.78 of
cumulative-to-50bps candidate capacity but kept it shadow-only until evidence and priors
could be attached. Capacity evidence was therefore not absent; it repeatedly arrived before
profit evidence and forced the route to stay below live-capital language.

## 7. Anchoring Uncertainty as Trading Constraint

An LLM prior near the market price is not independent just because the system labels it
"prior." Anchoring uncertainty is a trading constraint, narrower than a claim about LLM
truthfulness and narrower than a claim about market efficiency.

MarketAnchor v0.1.2 measured consensus-anchor sensitivity in one stored prediction-market
forecasting run. The headline mean net signed drift was 256.73 probability basis points
across 75 triplets, with high-anchor movement larger than low-anchor movement.

The sister paper's disclaimer is reproduced here in substance because it is central to
proper use: the statistic is not expected-return bps, not realized alpha, not calibration
error, and not trading profit without a separate portfolio model. The fifth disclaimer is
explicit: it is not a forecast-accuracy result. MarketAnchor measures how forecasts move
under anchor framing; it does not say whether the unanchored forecasts resolve correctly.

Paper 2 uses that result only for one proposition: if a prompt exposes market consensus and
then asks an LLM for an independent prior, the elicited prior can be contaminated by the
prompt itself.

The trading argument is separate and comes from Paper 2's corpus. If a strategy's apparent
LLM-prior edge is below roughly 500 bps, and if the prior was elicited near market-price or
consensus context, the edge is operationally contaminated unless anchor controls are applied.

The 500 bps figure is not borrowed from MarketAnchor as a return threshold. It is a
conservative operational buffer over a 256.73 bps descriptive drift and over the
narrative-trade observation that ablation deltas can be hundreds of bps.

llm-narrative-trade-0125 shows the applied problem. Market-quote inclusion and omission
changed priors, but the resulting gaps mixed signal, source quality, prompt sensitivity, and
model nondeterminism.

In R1, the prompt exposed the current market quote before the LLM emitted the prior. The row
schema appeared to place the prior timestamp before the market-quote timestamp, but the model
had already seen the quote. That is why this paper treats prompt ordering as a semantic
constraint, not only a timestamp constraint.

In R2, peer review identified the direction of the effect: with-quote priors moved toward
the market quote in seven of eight events. This is more specific than generic sycophancy. It
means a model can absorb visible consensus as if it were authoritative evidence and blend it
into the prior even when the route needs an independent estimate.

The R2 same-run variance also matters. Peer review reported mean sigma_without near 5.6
percentage points across three Codex CLI subprocesses. That variance is larger than the
200-bps to 500-bps edge bands that many retail strategies would try to monetize. A single
LLM number therefore cannot be treated as a calibrated probability without ensemble and
stability checks.

The trading implication is a noise-floor rule. If the measured anchor drift is roughly
256.73 probability bps in the sister artifact, and if the campaign-specific ablations show
hundreds or thousands of bps of movement in some rows, a claimed edge near the market has to
clear a larger buffer. The paper uses 500 bps as an operational threshold for suspicion, not
as a universal profit cutoff.

This buffer is intentionally conservative. It leaves room for a route with a very large
source-grounded disagreement, a stable no-quote prior, and enough book depth to survive. It
does not leave room for a row where the model saw the market quote, moved toward it, and then
reported a 200-bps gap as independent alpha.

The engineering response is paired prompts, anchor-masked priors, source-grounded evidence,
ensemble variance reporting, and capacity-weighted backtests. A single LLM prior near a
market price is not independent alpha.

The quote bank ties the anchoring constraint to specific prompt and prior failures: Q019
abelian/runs/2026-05-03-1900-profit-search/round-1/peer-B.txt:L26-L26; Q020
abelian/runs/2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L15-L15; Q021
abelian/runs/2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L16-L16; Q022
abelian/runs/2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L17-L17; Q023
abelian/runs/2026-05-04-0125-llm-narrative-trade/round-2/peer-A.txt:L18-L18.

This finding is a constraint, not a kill switch. LLM priors can still be useful as one
feature, especially when external evidence is strong and anchor exposure is controlled. The
corpus shows that uncontrolled priors are too unstable for small-edge trading claims.

The safest interpretation is operational. The relevant test is whether an LLM-prior trading
system keeps its prior materially stable when visible market consensus is hidden, perturbed,
or counterbalanced by source-grounded evidence. It also has to show that the stable prior
improves the actual trading ledger after fees, spreads, holding periods, and capacity are
included.

This is also why MarketAnchor is not used as a substitute for the Paper 2 corpus. The sister
artifact supplies a descriptive anchor-sensitivity measurement and the SHA
8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27 for reproducibility.
The trading conclusion comes only after the Abelian campaigns expose how prompt sensitivity
interacts with source quality, book depth, and realized execution.

## 8. Abelian Methodology Contribution

What does an adversarial loop actually do for an agentic research program? In this corpus,
it turns vague intent into a contract, rejected routes into auditable evidence, and
post-hoc confidence into a sequence of attacks that can be counted. The methodology
contribution is the empirical formalization of the Abelian adversarial loop: rule #16 R0
program gates, asymmetric peer policy, mission-thread route memory, commit-gate progress
checks, and frame-break protocol.

The earliest observed R0 program-gate artifact in this corpus is cross-platform-pilot-b at
2026-05-04T01:01:07Z. The methodology timeline identifies the file
`round-0/program-peer-challenge.txt` and records UTC mtime
`2026-05-04T01:01:07.208905+00:00`. Before that point, most campaigns had adversarial
review after mutation rather than before launch.

The R0 gate hardens the contract before the loop spends its first real round. The program
states the target, eval, metric, budget, files in scope, data gates, and stop conditions; the
baseline eval runs before mutation; a program-peer challenge attacks the contract before R1
starts; the contract hash records the launch boundary; and the TTY confirmation records that
the human operator accepted it. The steps are procedural, but their effect is empirical:
they make pre-launch ambiguity visible.

The gate's value is not that it guarantees success. Its value is that it makes launch
defects countable before a round spends engineering time on a fuzzy target, an unverifiable
metric, or a borrowed source of authority. In this corpus, plan-level attacks often mattered
more than code-level attacks because the route could fail before any implementation existed.

Path C records the clearest R0 trajectory. The initial challenge found 18 attacks across
target, eval, metric, scope, and borrowed-authority classes. The second version narrowed the
remaining blockers to 3. The third version left 1 residual issue. The fourth version reached
0 launch blockers and permitted R1.

The Path C attack sequence was not cosmetic. The early attacks forced the program to specify
EDGAR form coverage, evidence-grounded extraction, special-situation tradeability, cost
limits, and how confidence would be interpreted. R1 still failed on implementation, but it
failed against a more explicit contract. That difference is methodologically important: the
peer review could say exactly which promises were broken.

The Path C per-round meaning is visible in the contraction. The 18-attack round said the
program was not ready to launch because the parent target, eval semantics, evidence
grounding, and routeability gates were under-specified. The 3-attack round meant the main
shape was now testable but still had blocking ambiguities. The 1-attack round meant a single
residual launch issue remained. The 0-attack round did not certify profit; it certified that
R1 could fail against a named contract.

Paper 2 records a longer R0 trajectory. The prompt-side sequence produced 21 attacks, then
6, then 4, then 3, then 1 before R1 extraction. The later rounds narrowed the paper target
from a vague retrospective into a corpus-bound manuscript with line-count, citation, schema,
AI-disclosure, and arXiv-verification gates.

The methodology-self-attack file turns that trajectory into a costed gate record. It
contains 21 Paper 2 R0 self-attacks: 3 BLOCKER, 15 MAJOR, and 3 MINOR. The blocker-or-major
set includes target parent directories, contradictory section counts, an R1 plan that could
leave `main.md` absent while the eval stayed at zero, unsupported state extraction across
17 campaigns, empty legacy round directories, regex-only citation counting, missing
transcript provenance, v0.1.2 borrowed-credit errors, infrastructure/trading scope
confusion, and depth/budget mismatch. At a conservative 0.5 hours of R1 burn per
blocker-or-major defect, those 18 pre-R1 catches avoided roughly 9 hours of work that would
otherwise have produced uncommittable or reviewer-rejected artifacts.

The Paper 2 per-round meaning is different because the artifact is a manuscript rather than
a trading scanner. The 21-attack round challenged corpus definition, active-campaign counts,
claim scope, citation authority, and whether paper self-attacks could contaminate trading
findings. The 6-attack and 4-attack rounds narrowed the target to a data-backed
retrospective. The 3-attack round forced clearer evaluation and disclosure. The final
1-attack round left a bounded residual issue before R1 extraction. That sequence is why the
paper treats its own construction as methodology evidence.

The Paper 2 trajectory also shows a weakness of eval-only thinking. R2 later scored 100
under the then-current eval while containing many repeated paragraphs. Peer attack identified
the padding, and R3 added a uniqueness gate that caps the score at 75 when paragraph
uniqueness falls below 0.85. The methodology contribution is therefore not "evals solve
quality." It is that adversarial review and evals attack each other.

The asymmetric peer policy is a second method contribution. Claude peer-A is assigned
framing, scope policing, reviewer anticipation, and strategic plausibility. Codex peer-B is
assigned heavy extraction, transcript mining, recomputation, implementation, and verification.
The roles are not symmetric stylistic labels. They expose different failure surfaces.

The asymmetry matters in this paper because peer-A and peer-B caught different classes of
defect. Peer-A repeatedly pressed claim scope, reviewer framing, and hidden generalization
risks. Peer-B repeatedly pressed file-line provenance, schema validity, duplicated prose,
quote-bank quality, and exact eval behavior. A single generic peer role would have been less
likely to cover both.

The policy is also bounded. Peer-B does not get to solve reviewer framing by adding more
prose without evidence. Peer-A does not get to approve a claim because the story is elegant.
Each role has a different way to say no, and the campaign advances only when the selected
route survives both kinds of attack.

Mission threads force rejected routes to stay auditable. Each round records the goal
paraphrase, candidate routes, selected route, selection reason, metric delta, blocker
status, exploration flag, and frame-break count, so a route's silent disappearance becomes a
methodological violation rather than a clean restart.

The mission-thread rule is not bureaucracy. It is a guard against invisible p-hacking of the
research process. If the model considered a shallow metadata-only route, a prose-only route,
or a data-only route, the state file keeps that fact. The selected route then carries a
reasoned comparison against alternatives, not a retrospective story that only the winning
path was ever available.

The commit gate then asks for goal progress rather than activity. In this paper, that
distinction matters because many campaigns produced code, tests, tables, or prompts while
still failing to produce profit evidence or tradeable capacity. A round can be technically
busy and strategically null. The commit gate keeps that distinction visible.

A profitable-trading campaign therefore cannot count a scanner as progress unless it moves a
pool metric, reaches a verified paper-entry gate, or removes a named blocker on the path to
that gate. A paper campaign cannot count lines as progress unless they advance a claim with
evidence. R2's padding failure is the negative control that makes the rule concrete.

The frame-break protocol matters when repeated rounds converge on no route. It asks the loop
to change frame before declaring termination, but it does not permit unlimited scope
expansion. A frame break can move from public scraping to broker calls, or from LLM priors to
smart-money signals, only if the new frame names a different mechanism and a measurable gate.

Bankruptcy-operator gives an example. The public-scrape route did not expose enough
claim-specific capacity. A valid frame break would ask for executable broker quotes and
transfer mechanics for named classes. It would not add another generic scraper and call that
creativity. The frame break is a disciplined mechanism change.

Path C and Paper 2 also show that R0 gates can be multi-round objects. A single peer
challenge is useful, but the stronger pattern is challenge, rewrite, re-challenge, and only
then launch. The sequence turns vague disagreement into a counted convergence process. A
contract that begins with 21 attacks and launches with 1 residual issue has a visible
hardening trajectory.

This differs from conventional human-led adversarial review in one specific way. The review
is not only a post-hoc paper critique or a code review checklist. It is a mutation loop with
state, evals, route memory, and explicit stop conditions. The paper does not claim this is
better than expert human review. It claims the local corpus provides an instrumented record
of how such a loop changes research behavior.

The method is also not fully pre-registered for all campaigns. Most analyzed campaigns were
born before rule #16 was routine. Their peer files still contain adversarial critique, but
the critique mostly happens after mutation. Path C and Paper 2 are the cleanest examples of
pre-launch contract hardening under the R0 gate.

That chronology is why Section 3 separates trading evidence from methodology evidence. A
pre-gate campaign can support a claim about a trading mechanism if its artifacts are
sourceable and fillable. It cannot support the claim that the route was pre-registered under
rule #16. Conversely, Paper 2 self-attacks can support the methodology contribution while
remaining quarantined from cross-campaign trading recurrence counts.

The methodology timeline records this boundary explicitly. It lists the pre-2026-05-04
campaigns as retrospective, identifies the first R0 gate artifact, describes 2026-05-04
adoption, and records the 2026-05-05 spread into Path C and Paper 2. This prevents the paper
from smoothing an evolving method into a uniform protocol.

The supporting methodology evidence is therefore distributed across three local artifacts:
the timeline, the state files, and the peer transcripts. The timeline proves chronology. The
state files prove route memory and metric updates. The peer transcripts prove that attacks
were concrete enough to change implementation or claims.

The result is a paper-level contribution rather than merely a lab anecdote. The loop makes
failed trading campaigns legible as data, preserves alternatives that did not win, separates
infrastructure hardening from profit evidence, and exposes eval gaming when it appears. That
combination is the Abelian methodological claim.

The claim is still bounded. The corpus does not prove that Abelian review dominates other
research workflows. It does show that in this lab, the method repeatedly found hidden
assumptions before live capital, forced route-specific evidence requirements, and made
retrospective failures easier to analyze without converting them into heroic success stories.

## 9. Discussion

### 9.1 Findings Integration

The strongest paper claim is not that LLM trading cannot work. It is that the retail routes
that looked easiest for LLMs shared the same trap: LLM-accessible features are usually
accessible to other market participants, and LLM-extracted fields can lack source grounding
exactly where trading requires it.

The four findings form one mechanism chain. Math-arb saturation covers public price
relationships after obvious violations are visible: 8 of 11 trading-focused campaigns
explored math-arb-class or adjacent market-structure routes, and 0 of 8 produced sustainable
greater-than-$1k/month evidence after current-data, fillability, and capacity gates. The
negative result is balanced by positives: the 327-trade threshold-ladder arsenal was real
historical alpha, bydate LP arb survived in tiny size, and cross-platform scans measured real
but sub-floor cycle economics.

The ceiling-pin finding covers prompt-accessible or rubric-accessible fields that looked
high-confidence without source binding. The n=3 instances are supported by more than 12
direct source rows across llm-deploy, Path C, and llm-narrative-trade. The capacity ceiling
then turns "edge" into deployability: the corpus records $5.34 bottleneck depth, $200 to
$500 single-row deployability, $3k to $6k daily deployability under a 30-row assumption,
$0.32/day public LP-arb capacity on $100k, and an $85,446.78 shadow capacity frontier that
still lacked priors and current evidence.

Anchoring uncertainty supplies the fourth gate. The narrative-trade campaign shows both
positive and negative evidence: prompt engineering moved priors and R3 produced six newly
flagged rows, but the same implementation log recorded zero 24-hour PnL rows backfilled.
That is an engineering primitive, not realized trading profit.

The route registry completes the integration. Aggregate state counts 228 proposed routes;
135 were rejected, a 59.2% rejection rate. The recovered JSONL registry holds 225 rows: 45
selected, 135 rejected, and 45 deferred. Quote-bank quality improved too: 40 verbatim rows,
eight max per campaign, and peer-B capped at 24 of 40 quotes so cron-fill/ws-cron
infrastructure could not dominate the evidence base.

A candidate strategy therefore earns trading language only after it survives current-data
falsification, source-grounded extraction, capacity-weighted execution, and anchor-stable
prior estimation. Many ideas produced useful research artifacts before clearing all four
gates. That is the central evidence, not an embarrassment to hide.

### 9.2 Implications for Builders

For builders, the findings translate into gate order. Filing-evidence grounding belongs
before any confidence score; otherwise the rubric merely reports back the LLM's surface
plausibility. If a field cannot return a source span that a verifier can grep, the row is
not tradeable. The recovered promoted-route registry contains 10
evidence/source/filing/grounding routes, the repair family Path C needed after its R2
hallucinated pass row.

LLM priors belong behind anchor-masked prompts before any visible market quote or consensus
estimate is introduced. With-quote prompts remain useful as diagnostics, but the canonical
alpha source is generated, stored, and variance-checked before comparison to the market.
Sixteen promoted recovered routes mention priors, quotes, anchors, ablation, or consensus.

Backtests start as capacity-weighted objects. A strategy that clears a probability threshold
but fails on depth, fee drag, spread, holding period, or exit latency has not found deployable
alpha at the claimed bankroll. Thirty-nine promoted recovered routes mention capacity,
backtest, depth, fill, fee, spread, settlement, or PnL. That count is the builder lesson:
capacity is part of the first gate.

Adversarial review also has a sample-bias job. It asks whether the route was selected
because it was available, whether failed rows were dropped, whether historical violations
came from stale snapshots, and whether a live system would have known the same facts at the
same time. The rejected pile shows why: high-estimate routes such as multi-connection
sharding often lost to lifecycle, watchdog, observability, or blast-radius blockers.

The constructive role for LLMs is still large: source-span retrieval, rule-text
normalization, anomaly triage, hypothesis generation, and adversarial review. A trade
inherits the LLM output only after a non-LLM gate confirms the relevant source and execution
facts.

### 9.3 Methodology Generalization

Abelian rule #16's R0 gate is not specific to prediction-market trading. It is a mechanism
for agentic research loops where an incorrect launch is expensive: a trade, a production
deploy, a benchmark claim, or a public paper.

The empirical record supports testing that broader use. Path C narrowed 18 program-gate
attacks to 3, then 1, then 0 before the campaign proceeded. Paper 2 narrowed 21 attacks to
6, then 4, then 3, then 1 before R1 extraction. In both cases, the launch gate caught
critical defects before R1 burn: target parents, elastic eval semantics, borrowed
citations, scope creep, empty inventory, and evidence-definition mismatch. The methodology
timeline records the first observed R0 gate artifact at 2026-05-04T01:01:07.208905+00:00.

Those reductions do not prove future success; they show that pre-mutation challenge catches
scope, citation, metric, and evidence defects while they are still cheap to fix. Natural
non-trading inheritors are data releases, benchmark construction, infrastructure migration,
compliance-sensitive automation, paper submission pipelines, and agentic deploy loops. The
right measurement is defects caught before implementation, not only the final score.

### 9.4 What Is Not Claimed

The paper does not claim that prediction markets are efficient; it claims only that the
sampled retail routes did not clear the observed gates in this single-lab corpus. It does
not claim that LLMs cannot trade; it claims that these LLM-assisted routes did not become
sustainable greater-than-$1k-per-month retail trading systems after adversarial review.

The paper does not claim that n=3 ceiling-pin observations are universal. It does not claim
that Abelian methodology guarantees success. It does not claim that MarketAnchor v0.1.2's
256.73 probability-bps drift is tradable, that the unanchored priors were accurate, or that
the sister artifact proves realized edge.

The four findings are single-lab, single-period observations. The correct use is a boundary
map and an operational checklist, not a theorem about all prediction markets, all LLMs, or
all future market regimes.

## 10. Limitations

### 10.1 Single-Lab, Single-Operator, Single-Period

The study is single-lab, single-operator, and single-period. Stephen Wang ran the campaigns
at Abel AI Lab in 2026-Q2 using Claude general-purpose Agent and Codex CLI gpt-5.5 xhigh as
the main adversarial tools. No independent replication is claimed.

### 10.2 Ceiling-Pin Sample Size

The ceiling-pin count is n=3 cross-mechanism observations, suggestive not structural. The
cleanest count is n=2 if a reader requires only extraction systems: llm-deploy and Path C.
The n=3 version adds llm-narrative-trade-0125 because the prompt-gate actionability surface
is the same defect family, but that inclusion is not a universal law.

### 10.3 Stephen-Curated Selection Bias

The corpus is Stephen-curated and therefore subject to selection bias. It overrepresents
strategies that were plausible to one operator at one lab and underrepresents routes outside
that operator's attention, access, or taste. The sample is not a random draw from all
possible LLM-trading attempts.

### 10.4 Campaigns Predating the Formal R0 Gate

Most campaigns predate the mature rule #16 R0 gate. They contain adversarial review and
state artifacts, but they did not all begin under the same formal pre-mutation contract
discipline. This matters because methodology evidence is strongest when the gate is applied
before route selection, not reconstructed after the fact.

### 10.5 Reproducibility Pending License Confirmation

Public-source coverage is incomplete at draft time. Some source artifacts are local run
files and memory notes. Public release is planned, but the reproducibility package remains
pending license confirmation and repository publication. External reviewers without the
repository will need the release bundle before they can reproduce the same provenance
checks.

### 10.6 Four-Active-Day Execution Span

The active execution span is short. The inventory covers a 12-calendar-day window, but the
actively executed campaign span is four active days: 2026-05-02 through 2026-05-05. Many
findings emerged under compressed time pressure, and they may not generalize to slower
research programs that revisit routes over weeks or months.

### 10.7 LLM-Family Generalization Caveat

The LLM-family generalization is limited. The observations come from Codex CLI gpt-5.5 xhigh
and Claude general-purpose Agent, both from the same broad RLHF-era family of general-purpose
assistant models with similar alignment objectives. Findings may differ for base models,
Gemini-family systems, open-weight models, Llama, Mistral, domain-finetuned financial
models, or deterministic API configurations with seeds; the ceiling-pin failure mode could
be amplified or reduced under different RLHF priors.

### 10.8 Survivorship Bias

The corpus also has survivorship bias. Campaigns that died at R0 gate refusal or before any
logged round are not in the active corpus, so the analyzed 13-active-campaign set is biased
toward efforts that produced enough artifacts to inspect. Of 17 raw campaign directories,
four legacy directories contain eight empty round directories in total:
`bankruptcy-operator`, `cftc-event-fragmentation`, `crypto-bankruptcy-claims`, and
`llm-narrative-trade` (`per-campaign-summary.csv:L15-L18`); they keep the denominator honest
but are too empty to support mechanism claims, while ideas that died before creating even an
empty round directory remain invisible.

### 10.9 Post-Hoc Methodology Rationalization

The methodology claim is partly post-hoc. Abelian rule #16's R0 gate emerged mid-session,
with the first observation recorded at 2026-05-04T01:01:07Z. Path C and Paper 2 are the
cleanest examples fully pre-registered under the formal gate; the other 11 active campaigns
are analyzed retrospectively. Section 8 is therefore a calibrated methodology contribution,
not proof that the whole corpus was designed under the final gate.

### 10.10 Eval-Gaming as Internal Lesson

The eval-gaming caveat is internal and material. The Paper 2 R2 round produced metric=100
with 117 padded paragraphs before peer attack exposed the failure. The updated uniqueness
gate is a repair, not proof that future metrics cannot be gamed. Any LLM-output benchmark
that scores prose without uniqueness, provenance, and substantive-contribution gates remains
gameable, making this both a limitation of the draft process and a concrete methodological
lesson for agentic research evaluation.

## 11. Open Problems and Future Work

Can an anchor-controlled LLM prior survive perturbation and still improve a ledger? The next
study elicits priors with hidden, visible, counterfactual, and source-grounded market
contexts, then tests whether any edge survives the full perturbation set. It reports
no-quote canonical priors, with-quote drift, ensemble variance, and realized after-fee PnL
separately.

Can special-situation extraction stay high-confidence after the verifier leaves the model's
output and checks the filing or rule text itself? A filing or rule field is accepted only
when the system returns the source span and the verifier can grep the span before scoring
confidence. The next Path C-style run compares output-grep, filing-grep, and human-verified
rows, then reports how many high-confidence candidates survive each gate.

Can participant behavior supply a better signal class than model narration? Insider Form 4
and 13F changes, crypto whale flows, unusual options volume, borrow-rate moves, and
order-flow imbalance differ from LLM prior extraction because the information source is
behavior rather than prose. The probe is timestamped, leak-checked, and capacity-weighted
from the start.

The existing corpus contains the motivation but not yet the route registry row for this
mechanism.
Path C's compound handoff names a future Path D with insider transactions, options flow, or
satellite data as a different source class
(`2026-05-05-path-c-1week-probe/COMPOUND_DOC.md:L60`). That absence is itself a clean open
problem: the next route registry needs an explicit participant-behavior lane instead of
relying on LLM narration or public price fields.

What makes a cross-venue spread executable rather than merely visible? Cross-platform spread
ideas need synchronized fee models, withdrawal and settlement latency, order-book depth,
venue-specific fill constraints, and rule-semantics matching before alpha language is
warranted. A useful study fails rows independently on each axis rather than reporting a
single aggregate spread.

Do ceiling-pins survive a change in model family? The llm-deploy and Path C findings need
reruns on base models, Gemini-family models, open-weight Llama and Mistral systems, and
domain-finetuned financial models. The experiment tests whether rubric-side and prompt-side
ceiling-pins persist when models differ in training, alignment, determinism, and tool-use
behavior. Moving from n=3 to a stronger claim requires this replication.

Where does the capacity ladder change once the bankroll leaves retail scale? The paper maps
the retail-bankroll transition from $1k smoke tests to $100k utilization pressure. It does
not map institutional, HFT, or principal-book regimes. A follow-on study separates retail
API execution, professional market-making, broker-mediated OTC operation, and principal
inventory risk.

## Acknowledgments
External editorial and methodological feedback from independent paper-review consultations
improved metric naming, R1/R2 protocol stratification, contract-cluster sensitivity
analysis, AI/tool author-policy disclosure, and related-work coverage before submission.

## References
Full BibTeX entries are in references.bib. MarketAnchor v0.1.2 remains [citation pending
verification] until an external identifier exists.

## Reproducibility Appendix

Primary repository: Abel AI Lab polymarket_paper_trade-ws (analysis code under ws/, Abelian
campaigns under abelian/runs/).

Git commit analyzed: e361f9903a0e1f5fd06ee218950c662dbe1190f1

Cross-campaign aggregate file:
docs/research/paper-2-llm-extraction-and-pm-saturation/cross-campaign-aggregate.json

Attack registry:
docs/research/paper-2-llm-extraction-and-pm-saturation/anc/attack-registry.jsonl

Methodology self-attacks:
docs/research/paper-2-llm-extraction-and-pm-saturation/anc/methodology-self-attacks.jsonl

Alternative-route registry:
docs/research/paper-2-llm-extraction-and-pm-saturation/anc/alternative-routes.jsonl

Quote bank: docs/research/paper-2-llm-extraction-and-pm-saturation/anc/quote-bank.jsonl

MarketAnchor v0.1.2 cross-cite SHA256:
8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27

Public release plan: GitHub repository under Abel AI Lab plus Zenodo DOI for archival;
release pending license confirmation. Estimated release date: within 2 weeks of arXiv
submission.
