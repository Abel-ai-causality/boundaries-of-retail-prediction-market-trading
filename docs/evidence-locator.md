# Evidence Locator — Paper 2 v0.2.0

This file maps every numeric claim and named campaign in `docs/main.md`
to the exact source artifact that produced it. The locator exists so a
reviewer can audit a claim without re-deriving its provenance from the
manuscript prose, and so a future reader can verify that the
denominator-preserving corpus is not just narrated but indexable.

The locator is supplementary; it does not extend the paper's claims. If
a row looks light, the right move is to inspect the source artifact, not
to read the locator as evidence in itself. Where a recomputation is
trivial, the locator includes the one-line shell command.

## Schema

| Column | Meaning |
|---|---|
| Claim | Verbatim or paraphrased numeric / named claim from `main.md` |
| §  | Section in `main.md` where the claim appears |
| Source | Repository path that grounds the claim |
| Recompute | Optional shell command that re-derives the value from the source |

Paths are relative to the repository root. Section numbers refer to the
`# Section` headings in `docs/main.md` (the lead Abstract is `Abs`).

## A. Corpus card (Table 1, §1, §3)

| Claim | § | Source | Recompute |
|---|---|---|---|
| 17 raw campaign directories | §1 | `data/cross-campaign-aggregate.json` | `python3 -c "import json; print(len(json.load(open('data/cross-campaign-aggregate.json'))))"` |
| 13 active campaigns | §1, Table 1 | `data/cross-campaign-aggregate.json` | `python3 -c "import json; d=json.load(open('data/cross-campaign-aggregate.json')); print(sum(1 for r in d if r['instrumentation_level'] in ('full_state_json','peer_files_only')))"` |
| 4 sparse legacy directories | §1, §3 | `data/cross-campaign-aggregate.json` | `python3 -c "import json; d=json.load(open('data/cross-campaign-aggregate.json')); print(sum(1 for r in d if r['instrumentation_level']=='empty_legacy'))"` |
| 12 full-state-json + 1 peer-files-only | §3 | `data/cross-campaign-aggregate.json` | `python3 -c "import json,collections; d=json.load(open('data/cross-campaign-aggregate.json')); c=collections.Counter(r['instrumentation_level'] for r in d); print(dict(c))"` |
| 156 instrumented rounds (active total) | §1, Table 1, §3 | `data/cross-campaign-aggregate.json` (`n_rounds` over active rows) | `python3 -c "import json; d=json.load(open('data/cross-campaign-aggregate.json')); print(sum(r['n_rounds'] for r in d if r['instrumentation_level'] in ('full_state_json','peer_files_only')))"` |
| 225 recovered route decisions | §1, Table 1, §3 | `data/anc/alternative-routes.jsonl` (one row = one decision) | `wc -l < data/anc/alternative-routes.jsonl` |
| 45 selected / 135 rejected / 45 deferred | §3 | `data/anc/alternative-routes.jsonl` (`ultimate_outcome` field) | `python3 -c "import json,collections; print(dict(collections.Counter(json.loads(l)['ultimate_outcome'] for l in open('data/anc/alternative-routes.jsonl') if l.strip())))"` |
| 79 promoted routes (per-row promotion flag) | §3, Fig 2 | `data/anc/alternative-routes.jsonl` (`promoted_to_next_round=true`) | `python3 -c "import json; print(sum(1 for l in open('data/anc/alternative-routes.jsonl') if l.strip() and json.loads(l).get('promoted_to_next_round') is True))"` |
| 228 alternative-route rows (campaign aggregate, distinct metric) | §3 | `data/per-campaign-summary.csv` (`alternative_routes_count` column, summed across 17 raw campaigns) | `python3 -c "import csv; print(sum(int(r['alternative_routes_count'] or 0) for r in csv.DictReader(open('data/per-campaign-summary.csv'))))"` |
| 52 strict attack rows | §1, Table 1, §3 | `data/anc/attack-registry.jsonl` | `wc -l < data/anc/attack-registry.jsonl` |
| 40 quote-bank rows | §1, Table 1, §3 | `data/anc/quote-bank.jsonl` | `wc -l < data/anc/quote-bank.jsonl` |
| 0 durable deployment routes | Table 1, Abs, §1 | Negative claim derived from §4–§7; cross-check against the `key_finding_one_line` column of `data/per-campaign-summary.csv` for each trading-focused campaign | `awk -F, 'NR>1 {print $1": "$NF}' data/per-campaign-summary.csv` |
| 11 trading-focused campaigns / 59 trading-focused rounds | §1, §3, Abs | `data/per-campaign-summary.csv` (rows whose `dominant_finding_class` is not `infrastructure`); see also `data/anc/methodology-timeline.md` for partition rationale | — |
| 97 infrastructure-hardening rounds | §1, §3 | `data/per-campaign-summary.csv` (rows whose `dominant_finding_class` is `infrastructure`) | — |

## B. Gates I+II — sourceability and fillability (§4)

| Claim | § | Source | Recompute |
|---|---|---|---|
| Threshold-ladder arsenal: 327 walk-forward trades over 14 months | §4 | `data/anc/quote-bank.jsonl` rows tagged `polymarket-threshold-arb` family | `grep -c 'threshold' data/anc/quote-bank.jsonl` |
| 0 violations across 4,365 live markets on 2026-05-03 | §4 | Snapshot recorded in `data/anc/methodology-timeline.md` (closing entry for math-arb saturation campaign) | — |
| Market-making 100 bps: 5/6 fills lost | §4 | `data/anc/quote-bank.jsonl` row from `2026-05-03-0245-ws-cron-alignment` | `grep -F '100 bps' data/anc/quote-bank.jsonl` |
| Market-making 200 bps: 0/3 winning | §4 | Same source | `grep -F '200 bps' data/anc/quote-bank.jsonl` |
| Market-making 300 bps: sample too small | §4 | Same source | `grep -F '300 bps' data/anc/quote-bank.jsonl` |
| Internal-feature routes underperformed market snapshot | §4 | `data/anc/attack-registry.jsonl` rows tagged `internal-features` | `grep -F internal-features data/anc/attack-registry.jsonl` |

## C. Ceiling-pin layer migration (§5)

| Claim | § | Source | Recompute |
|---|---|---|---|
| Definitions 1–3 (ceiling-pin / layer migration / ceiling-pin layer migration) | §5 | Manuscript-internal definitions; cross-mechanism evidence below | — |
| n=2 strict extraction/gating instances | §10 | (a) `llm-deploy-10k` rule-reader rubric; (b) Path C SEC special-situations R1→R2 rubric tightening | — |
| n=3 broader prompt-gate family | §10 | n=2 above plus narrative-prior trading prompt-order case | — |
| `llm-deploy-10k`: 25 points × 4 fields, every event cleared | §5 | `data/anc/attack-registry.jsonl` rows tagged `llm-deploy-10k` and `data/anc/quote-bank.jsonl` rule-reader entries | `grep -F llm-deploy-10k data/anc/attack-registry.jsonl` |
| Path C R1→R2 rubric tightening with "none required" allowlisting | §5 | `data/anc/attack-registry.jsonl` rows tagged `path-c-special-situations` | `grep -F special-situations data/anc/attack-registry.jsonl \| head` |
| Narrative-prior prompt-order anchor exposure | §5, §7 | `data/anc/attack-registry.jsonl` rows tagged `llm-narrative-live-deploy` and the §7 anchor-stability discussion | `grep -F narrative data/anc/attack-registry.jsonl` |

## D. Gate III — capacity (§6)

| Claim | § | Source | Recompute |
|---|---|---|---|
| Capacity equation $E_j=\min(C_j,B_j)(g_j-f_j-s_j-\varepsilon_j)$ | §6 | Manuscript-internal definition; inputs are gates, not estimated per row | — |
| Crypto-PM probe: ~$5.34 fillable NO depth | §6 | `data/anc/quote-bank.jsonl` row from `2026-05-03-2025-crypto-pm-probe` | `grep -F '$5.34' data/anc/quote-bank.jsonl` |
| 23.6% spread on $5.34 (visible vs deployable) | §6 | Same campaign R1–R4 ledger via `data/anc/attack-registry.jsonl` | `grep -F crypto-pm-probe data/anc/attack-registry.jsonl` |
| Narrative-prior single-row capacity ~$200–$500 | §6 | `data/anc/quote-bank.jsonl` rows from `2026-05-03-1710-cross-platform-pilot-b` / `llm-narrative-live-deploy-10k` | `grep -F llm-narrative data/anc/quote-bank.jsonl` |
| Bankruptcy-claim sourcing: access depth missing | §6 | `data/anc/attack-registry.jsonl` rows tagged `bankruptcy-operator` | `grep -F bankruptcy data/anc/attack-registry.jsonl` |
| pm-10k50k-profit: $85,446.78 cumulative-to-50bps capacity, 4 candidates | §6 | `data/anc/quote-bank.jsonl` rows tagged `pm-10k50k` | `grep -F '85,446' data/anc/quote-bank.jsonl` |

## E. Gate IV — anchor stability (§7)

| Claim | § | Source | Recompute |
|---|---|---|---|
| MarketAnchor v0.1.2 SHA-256 = `8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27` | §7, Reproducibility | Frozen sister artifact (publicly addressable by SHA) | — |
| 256.73 probability bps mean net signed drift | §7 | Sister artifact `MarketAnchor v0.1.2`; reproduced verbatim in `docs/sycophancy-benchmark-marketanchor-v0.1.2.md` (in-repo retrospective) | `grep -F 256.73 docs/sycophancy-benchmark-marketanchor-v0.1.2.md` |
| 75 matched triplets across 8 contracts | §7 | Same source | `grep -F triplet docs/sycophancy-benchmark-marketanchor-v0.1.2.md` |
| 500 bps operational hygiene buffer | §7 | Heuristic derived from the 256.73 bps observed drift plus campaign-specific ablation movements; defended in `docs/sycophancy-benchmark-marketanchor-v0.1.2.md` | — |

## F. Abelian methodology (§8)

| Claim | § | Source | Recompute |
|---|---|---|---|
| Path C R0 trajectory 18 → 3 → 1 → 0 attacks | §8 | `data/anc/methodology-self-attacks.jsonl` (Path C subset) and `data/anc/methodology-timeline.md` | `grep -c path-c data/anc/methodology-self-attacks.jsonl` |
| Manuscript R0 trajectory 21 → 6 → 4 → 3 → 1 attacks | §8 | `data/anc/methodology-self-attacks.jsonl` (paper-2 subset, 21 rows) | `wc -l < data/anc/methodology-self-attacks.jsonl` |
| Asymmetric peer roles (framing/scope vs extraction/recomputation) | §8 | `data/anc/attack-registry.jsonl` `peer_role` field | `python3 -c "import json,collections; print(dict(collections.Counter(json.loads(l)['peer_role'] for l in open('data/anc/attack-registry.jsonl') if l.strip())))"` |
| R0 program gate as preregistration analogue | §8 | Cited externally; closest formal analogue is Nosek et al. (2018), *Proceedings of the National Academy of Sciences* | — |

## G. Cross-paper integrity

| Claim | § | Source |
|---|---|---|
| Sister paper SHA-256 cross-citation preserved | Reproducibility Appendix | `8968953708979dc2bd2915ec5c0a22c40e730c24d8134470739b7084bec5ca27` (line 481-484 of `docs/main.md`) |
| 2026-Q2 corpus window | §1, §10 | All entries in `data/cross-campaign-aggregate.json` have `last_round_iso` within 2026-04 → 2026-05; `data/anc/methodology-timeline.md` records the partition closing date |

## Notes on residual uncertainty

The `97 infrastructure / 59 trading` round split and the
`11 trading-focused campaigns` count partition the active 13 / 156
active-rounds totals using the `dominant_finding_class` column of
`data/per-campaign-summary.csv` plus a small set of manual
classifications recorded in `data/anc/methodology-timeline.md`. Different
classification choices (e.g., placing `other` with trading versus with
infrastructure) move the split by at most a few rounds. The
denominator-preserving claim is robust to that choice; the partition
exists to keep engineering hardening from being mislabeled as trading
edge, not to support a fine-grained measurement.

The `79 promoted routes` is the per-row count of
`promoted_to_next_round=true` in `alternative-routes.jsonl`: routes that
were retained into a later round without being chosen as the
implementation path. The separate `228` aggregate in
`per-campaign-summary.csv` (`alternative_routes_count`) counts every
alternative-route row generated per campaign and is a different metric;
both are reported here so readers can recompute either.

If a reviewer finds an entry that does not reproduce, please open an
issue in the public repository with the manuscript line and the source
file consulted; the discrepancy is more useful than the certainty.
