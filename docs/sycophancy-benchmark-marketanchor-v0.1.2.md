# MarketAnchor: Measuring Consensus-Anchor Sensitivity in an LLM Forecaster

A matched-framing diagnostic for prompt-induced prior drift in prediction-market forecasting

Version: v0.1.2.
Author: Stephen Wang.
Affiliation: Abel AI Lab.
Email: lab@abel.ai.
License: CC BY 4.0 (pending Abel AI Lab approval before arXiv submission; license is irrevocable per arXiv policy and will be confirmed at submission time)
Date: 2026-05-05.

## AI and Tool Assistance Disclosure

Anthropic Claude was used for peer-challenge critique and benchmark-design review. OpenAI Codex was used for repository inspection, statistical recomputation support, and draft-editing assistance. OpenAI ChatGPT was used for editorial review and submission-readiness audit. The human author reviewed all outputs and accepts responsibility for the manuscript, statistics, code references, citations, and claims. These tools are not authors.

## Acknowledgments

External editorial and methodological feedback improved the metric naming, R1/R2 stratification, contract-cluster sensitivity analysis, and related-work coverage before submission.

## Abstract

MarketAnchor is a matched-framing diagnostic that tests whether an LLM forecaster's stated probability prior changes when an otherwise identical forecasting prompt displays a consensus-framed anchor.
We analyze 225 stored result rows from a benchmark run, corresponding to 75
complete three-prompt triplets over eight prediction-market contracts. Each
triplet contains an unanchored prompt, a low-anchor framing, and a high-anchor
framing; all analyzed rows use the Codex backend with model gpt-5.5 in the
prediction-market domain. Recomputing from the stored priors, the signed
net-drift statistic ((p_low + p_high)/2 - p_unanchored) * 10,000 has mean 256.7
probability basis points and median 250.0 basis points. A nonparametric
bootstrap over complete triplets gives a 95% confidence interval of [149.8,
367.2] basis points, and a one-sample t-test over triplets gives t(74) = 4.62,
p = 1.6e-5. The response is asymmetric: low-anchor prompts move priors downward
by 616.1 basis points on average, while high-anchor prompts move them upward by
1129.6 basis points. We emphasize that the signed statistic measures
prompt-induced prior drift, not forecast accuracy, calibration error, expected
return, or realized trading profit. The result is limited by one model/backend,
one active domain, mixed anchor protocols across run phases, and only eight
contract clusters. MarketAnchor is best read as a first-run diagnostic artifact
showing that market-facing LLM priors can be contaminated by consensus-framed prompt context.

## Background

Prediction-market trading systems increasingly use language models to convert
contract text, news, and historical context into probability priors. This is a
natural interface: the model reads a market question, produces a probability,
and downstream logic compares that probability with a market price. The same
interface creates a direct prompt-contamination channel. If the prompt includes
the market price or a public-consensus estimate, the model may not supply an
independent prior. It may instead move toward the displayed value.

MarketAnchor v0.1 measures whether an LLM forecaster changes stated probability
priors when an otherwise matched prompt displays a consensus-framed anchor.
This v0.1.2 revision preserves the original run artifact but renames the
measured quantity. The statistic in the result file is not a general
"sensitivity" magnitude, because symmetric low-anchor and high-anchor movements
can cancel. It is net signed drift: the signed movement of the average anchored
prior relative to the unanchored prior.

This report uses "sycophancy" only as a legacy benchmark label. The measured
construct is consensus-anchor sensitivity: movement in a stated probability
prior under prompt-visible anchor framings. This construct is different from
the common RLHF usage, where a model agrees with a user's belief or preference
in conversation. The MarketAnchor diagnostic instead asks whether a
forecasting prompt's visible consensus frame changes a probability prior for
the same prediction-market contract.

The report should be read as a first-run diagnostic artifact. It does not
estimate model-wide calibration. It does not establish trading alpha. It does
not show whether visible market prices help or hurt a final trading system.
It isolates a narrower measurement: within one stored run, did the displayed
anchor framing move the stated prior for otherwise matched prompts?

The answer in this artifact is yes. The combined run has a mean net signed drift of 256.73 probability basis points. The effect is large relative to
ordinary probability-reporting noise in this run, but the estimate should be
interpreted as a within-run diagnostic rather than a population-level model
property. It is within-run evidence that this single LLM
forecaster/backend/domain combination moved under consensus-framed prompts.

## Related Work

The closest methodological ancestors are anchoring-and-adjustment and framing
studies in human judgment. Tversky and Kahneman's work on heuristics and
decision framing established that numeric anchors can alter human estimates
even when the anchor is uninformative or only partially informative. Market
prices and prediction-market consensus values are more than arbitrary anchors,
but they can still act as prompt-visible reference points.

Recent LLM work has moved this question from human judgment into model
behavior. Lou and Sun study anchoring bias in large language models directly,
testing how numeric anchors affect model outputs. Huang et al. introduce the
SynAnchors setting, using synthetic data to study the anchoring effect in LLMs.
Those papers are directly relevant to MarketAnchor's construct, although
MarketAnchor differs by using matched prediction-market prompts and reporting
probability-prior drift in basis points.

Forecasting benchmarks are a second relevant line. Karger et al.'s
ForecastBench evaluates AI forecasting capability dynamically. Schoenegger et
al. study AI-augmented prediction and report improvements in human forecasting
with LLM assistants. Cheng, Liu, and Long introduce PolyBench, a live
prediction-market benchmark for LLM forecasting and trading capability. Yang
et al.'s Prophet Arena work studies predictive intelligence in an arena-style
setting. Halawi et al. analyze whether language models can use forecasting
strategies.

We did not identify prior work that isolates this exact matched-triplet
diagnostic: one unanchored prompt, one low-anchor framing, and one high-anchor
framing for identical prediction-market contracts, scored as stated-prior
drift. To our knowledge, MarketAnchor is the first reported matched-triplet
diagnostic focused specifically on prompt-visible market-consensus-style
anchors and their effect on an LLM forecaster's stated probability prior for
identical prediction-market contracts.

This novelty claim is intentionally narrow. MarketAnchor does not claim to be
the first LLM anchoring study, the first LLM forecasting benchmark, or the first
prediction-market evaluation. It contributes a small diagnostic design for the
intersection of those topics: market-facing LLM priors under visible consensus
anchors.

## Methodology

The benchmark pipeline is implemented in `ws/sycophancy_benchmark/runner.py`.
The runner defines three framings: `UNANCHORED`, `ANCHORED-LOW`, and
`ANCHORED-HIGH`. It iterates over requested domains, backends, questions, and
reruns. The analyzed result file contains only the `prediction_market` domain,
the `codex` backend, and model `gpt-5.5`.

The prediction-market domain is defined in
`ws/sycophancy_benchmark/domains.py`. The stored domain rows include Polymarket
Gamma API source URLs for the first six contracts and Kalshi source URLs for
the two later contracts that appear in this result file. Each stored row also
contains a `consensus_value`, a `consensus_source`, a `consensus_timestamp`, a
resolution date, and a `training_cutoff_safe` flag.

The LLM backend analyzed here is `CodexBackend`, with default model `gpt-5.5`
and high reasoning effort through the Codex CLI configuration. The prompt asks
for a JSON object containing `probability_prior` and short reasoning. The
parser recursively searches backend output for that JSON field and clips parsed
probabilities to the unit interval.

Each complete triplet contains one unanchored prompt, one low-anchor prompt,
and one high-anchor prompt for the same contract. The runner writes one JSONL
row per framing, so the 225 physical rows correspond to 75 complete triplets.
The triplet, not the physical row, is the primary unit for the within-run
estimate because the same triplet statistic is duplicated across the three
framing rows.

Notation:

| Symbol | Definition |
|---|---|
| `p_i0` | Stated probability prior for triplet `i` under the unanchored prompt |
| `p_iL` | Stated probability prior for triplet `i` under the low-anchor prompt |
| `p_iH` | Stated probability prior for triplet `i` under the high-anchor prompt |
| `L_i` | Low-anchor directional shift: `(p_iL - p_i0) * 10000` |
| `H_i` | High-anchor directional shift: `(p_iH - p_i0) * 10000` |
| `D_i` | Net signed drift: `((p_iL + p_iH) / 2 - p_i0) * 10000` |

All three quantities are reported in probability basis points. `L_i` is
expected to be negative when a low anchor pulls the prior downward. `H_i` is
expected to be positive when a high anchor pulls the prior upward. `D_i`
summarizes the average anchored prior's signed movement relative to the
unanchored prior. Because `D_i` is signed, equal downward and upward movements
cancel. It is therefore not a complete measure of anchor sensitivity by itself.

The reviewer-requested asymmetry statistic is:

`asymmetry = mean(H_i) - abs(mean(L_i))`.

A positive asymmetry means high-anchor prompts moved the prior upward more than
low-anchor prompts moved it downward, in average signed basis points. A
negative asymmetry would mean the low-anchor response dominated in absolute
average size.

The run contains two anchor protocols. R1 rows used true market consensus and
its complement. R2 rows used synthetic low/high anchors approximately
15 percentage points around the model's unanchored prior, clipped to the
interval used by the runner. The JSON rows do not have a `phase` field, but
the phase is identifiable by schema and ordering. The first 42 rows lack
`entry_id`, `anchor_value`, `anchored_low_value`, and `anchored_high_value`;
their prompt logs show the true consensus/complement protocol. The later
183 rows include those fields and `entry_id` values beginning with `r2:`.

Because R1 and R2 have heterogeneous treatment definitions, the combined
result is descriptive. R2 dominates the file with 61 of 75 triplets and is the
main estimate for the synthetic matched-anchor protocol. R1 is treated as a
historical pilot that demonstrates the earlier market-consensus/complement
framing, not as part of a homogeneous treatment.

Statistics were recomputed from the stored priors in `results.jsonl`, not from
the duplicated stored `sycophancy_bps` field. Consecutive three-row blocks were
used as preserved triplets because rerun indices repeat across appended run
phases. The primary bootstrap is a 10,000-resample nonparametric percentile
bootstrap over complete triplets with replacement, using the same deterministic
seed as the benchmark helper. The t-test is a two-sided one-sample t-test of
triplet-level `D_i` against zero.

Contract-cluster sensitivity was computed by aggregating triplet-level `D_i`
within each `question_id`. A sign test then counted whether the eight
contract-level means were positive. A cluster bootstrap resampled the eight
`question_id` clusters with replacement and included all triplets within each
sampled cluster when computing the bootstrap mean.

## Results

The headline descriptive result is a mean net signed drift of 256.73
probability basis points over all 75 triplets. The median is 250.00 bps. The
triplet-level bootstrap confidence interval is [149.80, 367.17] bps, and the
triplet-level one-sample t-test gives t(74) = 4.62, p = 1.59e-05.

The response is asymmetric. The low-anchor condition has mean directional
shift -616.13 bps, while the high-anchor condition has mean directional shift
+1129.60 bps. The asymmetry statistic is therefore 513.47 bps. This means that
the high-anchor upward shift exceeded the absolute low-anchor downward shift
by roughly 5.13 percentage points in average probability-basis-point terms.

| Statistic | Value |
|---|---:|
| Physical result rows | 225 |
| Complete three-prompt triplets | 75 |
| Distinct `question_id` clusters | 8 |
| Backend-domain cells | 1 |
| Model | `codex` / `gpt-5.5` |
| Domain | `prediction_market` |
| Mean net signed drift `D_i` | 256.73 bps |
| Median net signed drift `D_i` | 250.00 bps |
| Standard deviation, triplet level | 481.29 bps |
| Minimum / maximum `D_i` | -1200.00 / 2050.00 bps |
| Mean low-anchor shift `L_i` | -616.13 bps |
| Mean high-anchor shift `H_i` | 1129.60 bps |
| Asymmetry, `mean(H_i) - abs(mean(L_i))` | 513.47 bps |
| 95% bootstrap CI, triplets | [149.80, 367.17] bps |
| One-sample t-test, triplets | t(74) = 4.62, p = 1.59e-05 |

The unit-of-analysis distinction is material:

| Unit of analysis | Count | Role in this report |
|---|---:|---|
| Physical rows | 225 | Descriptive only; each triplet appears as three framing rows |
| Complete triplets | 75 | Primary within-run estimate |
| Contract means | 8 | Cluster sensitivity with fragile small-cluster inference |

Stratifying by protocol shows why the combined estimate should be interpreted
carefully. R2 has most of the triplets and a tighter estimate because it used
the synthetic matched-anchor protocol. R1 has only 14 triplets and much wider
uncertainty because it is a small historical pilot.

| Partition | Triplets | Mean `D_i` | Median `D_i` | 95% bootstrap CI | t-test |
|---|---:|---:|---:|---:|---|
| R1 historical pilot | 14 | 344.64 | 128.75 | [-146.43, 859.82] | t(13) = 1.29, p = 0.219 |
| R2 main protocol | 61 | 236.56 | 250.00 | [170.00, 299.59] | t(60) = 7.09, p = 1.76e-09 |
| Combined descriptive | 75 | 256.73 | 250.00 | [149.80, 367.17] | t(74) = 4.62, p = 1.59e-05 |

| Partition | Mean low shift `L_i` | Mean high shift `H_i` | Asymmetry |
|---|---:|---:|---:|
| R1 historical pilot | -292.14 bps | 981.43 bps | 689.29 bps |
| R2 main protocol | -690.49 bps | 1163.61 bps | 473.11 bps |
| Combined descriptive | -616.13 bps | 1129.60 bps | 513.47 bps |

The R2 result is the best single summary of the current matched synthetic
protocol. The combined result remains useful as a full-artifact description,
but it mixes true-consensus/complement anchors with synthetic anchors around
the model's own unanchored prior.

Contract-level aggregation shows that all eight contract means are positive.
The exact two-sided sign test over eight nonzero contract means gives
p = 0.0078125. The cluster bootstrap that resamples `question_id` clusters and
includes all triplets within sampled clusters gives a 95% confidence interval
of [142.33, 363.07] bps. Direction is stable at contract level, but inference
with eight clusters is fragile.

| Question ID | Triplets | Mean `D_i` | Mean `L_i` | Mean `H_i` | Asymmetry |
|---|---:|---:|---:|---:|---:|
| `pm_1393070` | 13 | 290.38 | 194.62 | 386.15 | 191.54 |
| `pm_1931112` | 5 | 230.00 | -1080.00 | 1540.00 | 460.00 |
| `pm_2132778` | 13 | 50.00 | -1146.15 | 1246.15 | 100.00 |
| `pm_564198` | 8 | 253.75 | -505.00 | 1012.50 | 507.50 |
| `pm_565064` | 13 | 296.15 | -730.77 | 1323.08 | 592.31 |
| `pm_599305` | 13 | 492.31 | -415.38 | 1400.00 | 984.62 |
| `pm_kalshi_cpi_26may_47` | 5 | 240.00 | -540.00 | 1020.00 | 480.00 |
| `pm_kalshi_fed_28jan_h0` | 5 | 40.00 | -1360.00 | 1440.00 | 80.00 |

The largest positive triplet-level observation is 2050.00 bps on the Detroit
Pistons market. The largest negative observation is -1200.00 bps on the
Bitcoin dip market. These tails widen the standard deviation, but they do not
determine the sign of the contract-level result: each contract-level mean is
positive after averaging all its triplets.

The directional-shift table also clarifies why `D_i` must not be described as
general anchor sensitivity. Some contracts have substantial low-anchor and
high-anchor movements that offset in the net signed statistic. For example,
the Federal Reserve contract has mean `L_i` of -1360.00 bps and mean `H_i` of
1440.00 bps, but its mean `D_i` is only 40.00 bps because the two directions
nearly cancel.

## Limitations

- The analyzed result file covers one LLM family and one backend only:
  `codex` with model `gpt-5.5`. No Claude, Llama, Grok, OpenRouter, or local
  open-weight model rows are present.
- The analyzed result file covers one active domain only:
  `prediction_market`. The planned `sports_outcomes` domain is defined in the
  repository but has zero rows in `results.jsonl`.
- The program contract targeted broader coverage than this artifact delivered.
  MarketAnchor v0.1.2 therefore reports a narrowed diagnostic, not a completed
  population benchmark.
- R1 and R2 use heterogeneous anchor construction. R1 uses true market
  consensus and complement anchors. R2 uses synthetic low/high anchors around
  the model's unanchored prior. The combined result is descriptive only.
- The physical N is 225, but the primary unit is 75 complete triplets, and
  those triplets are clustered within only 8 distinct contracts. Contract-level
  direction is stable, but small-cluster inference is fragile.
- The stored statistic is net signed probability-prior drift. It should not be
  interpreted as expected-return bps, realized alpha, calibration error, or
  trading profit without a separate portfolio model.
- Polymarket and Kalshi consensus values are not ground-truth probabilities.
  The benchmark measures movement relative to posted or synthetic
  consensus-framed anchors, not accuracy against eventual outcomes.
- The output parser and prompting stack are part of the measured system.
  Changes to JSON parsing, prompt wording, model routing, or reasoning-effort
  settings could change the estimate.
- The R2 synthetic anchors are generated after observing the unanchored model
  prior. This is useful for matched perturbation, but it means the anchor
  values are not always actual market prices.
- The result file is an append-phase artifact. Consecutive three-row grouping
  was required because rerun numbers repeat across phases.

The model name `gpt-5.5` is the backend model identifier recorded by the Codex configuration used in this run. Reproducing the exact backend behavior may require access to the same model endpoint, CLI configuration, and reasoning-effort settings.

## Discussion / Implications

The practical implication is narrow but direct. If an LLM-driven trading agent
includes a market consensus or price in its prompt and then treats the LLM
output as an independent prior, the prior can be contaminated by the prompt
itself. In this run, the combined artifact's mean net signed drift is about
2.57 percentage points, and the directional high-anchor shift is much larger.

This is not a 257 bps return estimate. Translating probability-prior drift into
trading edge requires position sizing, payoff structure, fees, slippage,
execution constraints, and calibration assumptions that are not estimated
here. A prompt-induced movement in a probability prior can matter operationally
without implying any realized profit.

For institutional users, the implication is narrower but operationally
important: a probability elicited from a prompt that exposes market price or
consensus should not be treated as an independent prior unless anchor
sensitivity has been measured and corrected. This does not imply that hiding
market prices improves trading performance; it means that a model output
elicited with visible market prices should not be treated as an independent
prior without an anchor-sensitivity correction.

MarketAnchor validates the diagnostic value of matched framing tests. An
unanchored prior and two anchored priors for the same contract reveal whether
the model is acting as an independent forecaster or as a conditional generator
whose output moves with prompt context. The asymmetry result is especially
important because the high-anchor response does not merely offset the
low-anchor response.

For benchmark designers, a matched anchor diagnostic should sit beside
accuracy, calibration, refusal rate, parsing reliability, and latency. It is a
cheap test relative to live trading risk and identifies a failure mode that can
otherwise be mistaken for model insight. For system designers, the measurement
suggests logging whether market price was visible, running holdout
anchor-sensitivity probes, and applying de-biasing or downweighting rules when
the response is large.

## Future Work

MarketAnchor v0.2 should first close coverage gaps. The backend failure that
blocked Claude rows should be fixed, and at least Claude, Codex, an open-weight
model, and another hosted model should be run under identical prompt templates.
The planned sports domain should be executed, and additional domains should
include macroeconomic releases, weather or climate thresholds, and
corporate-event markets.

The anchor protocol should be separated cleanly into named experimental arms:
real market consensus, complement of market consensus, synthetic low/high
anchors around the unanchored prior, and fixed-distance anchors around market
price. Each arm should be reported separately before any combined descriptive
summary is shown.

The metric set should also separate signed and unsigned constructs. Future
reports should publish `D_i`, `L_i`, `H_i`, `abs(L_i)`, `abs(H_i)`, and a
directional asymmetry measure. This would prevent a small signed drift from
masking large but symmetric anchor responses.

The benchmark should become longitudinal. Re-running the same protocol
quarterly would show whether later training rounds, prompting changes, or
product-level anti-anchoring interventions reduce the measured movement. The
reportable object should become a time series by model family, backend, domain,
anchor protocol, and anchor distance.

The reproducibility package should be public before citation. It should include
the exact result JSONL, prompt logs, response logs, market-data snapshots, and
analysis scripts. A Zenodo archive should preserve a release DOI so the paper's
numbers can be tied to immutable artifacts.

## References

1. Tversky, A., and Kahneman, D. (1974). "Judgment under Uncertainty:
   Heuristics and Biases." `Science`, 185(4157), 1124-1131.
   https://doi.org/10.1126/science.185.4157.1124
2. Tversky, A., and Kahneman, D. (1981). "The Framing of Decisions and the
   Psychology of Choice." `Science`, 211(4481), 453-458.
   https://doi.org/10.1126/science.7455683
3. Kahneman, D., and Tversky, A. (1979). "Prospect Theory: An Analysis of
   Decision under Risk." `Econometrica`, 47(2), 263-291.
   https://doi.org/10.2307/1914185
4. Lou, Y., and Sun, J., "Anchoring Bias in Large Language Models:
   An Experimental Study", arXiv:2412.06593, 2024.
   https://arxiv.org/abs/2412.06593
5. Huang, [first-author initial unavailable in source], et al., "Understanding the
   Anchoring Effect of LLM with Synthetic Data", arXiv:2505.15392, 2025.
   https://arxiv.org/abs/2505.15392
6. Karger, E., et al., "ForecastBench: A Dynamic Benchmark of AI
   Forecasting Capabilities", arXiv:2409.19839, 2024.
   https://arxiv.org/abs/2409.19839
7. Schoenegger, P., et al., "AI-Augmented Predictions: LLM Assistants
   Improve Human Forecasting Accuracy", arXiv:2402.07862, 2024.
   https://arxiv.org/abs/2402.07862
8. Cheng, L., Liu, Z., and Long, X., "PolyBench: Benchmarking LLM
   Forecasting and Trading Capabilities on Live Prediction Market Data",
   arXiv:2604.14199, 2026. https://arxiv.org/abs/2604.14199
9. Yang, [first-author initial unavailable in source], et al., "LLM-as-a-Prophet:
   Understanding Predictive Intelligence with Prophet Arena", arXiv:2510.17638, 2025.
   https://arxiv.org/abs/2510.17638
10. Halawi, D., et al., "Can Language Models Use Forecasting Strategies",
    arXiv:2406.04446, 2024. https://arxiv.org/abs/2406.04446
11. Perez, E., Ringer, S., Lukosiute, K., et al. (2022). "Discovering
    Language Model Behaviors with Model-Written Evaluations." arXiv:2212.09251.
    https://arxiv.org/abs/2212.09251
12. Sharma, M., Tong, M., Korbak, T., et al. (2023). "Towards Understanding
    Sycophancy in Language Models." arXiv:2310.13548.
    https://arxiv.org/abs/2310.13548
13. Wei, J., Huang, D., Lu, Y., Zhou, D., and Le, Q. V. (2023). "Simple
    Synthetic Data Reduces Sycophancy in Large Language Models."
    arXiv:2308.03958. https://arxiv.org/abs/2308.03958
14. Wolfers, J., and Zitzewitz, E. (2004). "Prediction Markets."
    `Journal of Economic Perspectives`, 18(2), 107-126.
    https://doi.org/10.1257/0895330041371321

## Reproducibility Appendix

Author and contact:
Stephen Wang, Abel AI Lab, lab@abel.ai.

Primary data artifact:
`abelian/runs/2026-05-04-sycophancy-benchmark/results.jsonl`.

Primary data SHA256:
`ad840b3be47871a7ba2c8a856f55d505d260e6f9ba42f76cfada1d3996c191b4`.

Git commit analyzed:
`e361f9903a0e1f5fd06ee218950c662dbe1190f1`.

Analyzed row count:
225 physical rows; 75 complete three-prompt triplets; 8 distinct
`question_id` clusters.

Benchmark code paths:
`ws/sycophancy_benchmark/runner.py`,
`ws/sycophancy_benchmark/backends.py`,
`ws/sycophancy_benchmark/domains.py`, and
`ws/sycophancy_benchmark/scoring.py`.

Analysis convention:
consecutive three-row blocks in `results.jsonl` were treated as complete
triplets because rerun identifiers repeat across appended phases.

Phase identification:
R1 rows are the first 42 rows and lack `entry_id` and anchor-value fields.
R2 rows are the later 183 rows and include `entry_id`,
`anchored_low_value`, and `anchored_high_value`.

Market data snapshots:
the JSONL rows store `consensus_value`, `consensus_source`, and
`consensus_timestamp` at query time. Public release should include the raw API
payload archive and its SHA256. The API payload archive hash is public-release
pending because no standalone payload archive was present in this workspace.

Public repository plan:
release the benchmark in a GitHub repository. Repository URL is public release
pending. Code should be licensed under Apache-2.0 or MIT.
License: CC BY 4.0 (pending Abel AI Lab approval before arXiv submission; license is irrevocable per arXiv policy and will be confirmed at submission time)

Archival plan:
create a Zenodo DOI for the public release containing the code, result JSONL,
prompt logs, response logs, market-data snapshots, and recomputation script.

No fresh LLM subprocess calls were made for this v0.1.2 revision. The
statistical analysis used only the stored result rows and preserved logs.
