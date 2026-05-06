# Data Dictionary

This directory contains the public-release data package for Paper 2.

## Provenance

The data was extracted from internal Abelian campaigns run by Abel AI Lab from
2026-04-24 to 2026-05-05. The public files are archival copies prepared for the
Paper 2 v0.1.0 release.

The data supports a single-lab, single-period retrospective. It should not be
read as a complete market-wide dataset.

## License

Proposed license before public push: CC BY 4.0. Stephen Wang and Abel AI Lab
confirm the final data license before release.

## `cross-campaign-aggregate.json`

Format: JSON array with 17 campaign objects.

Fields:

| Field | Type | Description |
|---|---|---|
| `run_id` | string | Internal campaign identifier |
| `instrumentation_level` | string | One of `full_state_json`, `peer_files_only`, or `empty_legacy` |
| `n_rounds` | integer | Round count represented for the campaign |
| `n_codex_files` | integer | Count of Codex-generated or Codex-associated files |
| `total_codex_bytes` | integer | Total bytes across Codex files |
| `n_peer_a_files` | integer | Peer-A transcript/file count |
| `n_peer_b_files` | integer | Peer-B transcript/file count |
| `campaign_status` | string | Campaign status at extraction time |
| `convergence_outcome` | string | Retained, terminated, or other campaign outcome label |
| `peer_convergence_count` | integer | Count of peer convergence markers |
| `terminate_no_route_count` | integer | Count of terminate-no-route markers |
| `flags_for_rN_count` | integer | Count of round-flag markers |
| `alternative_routes_proposed_count` | integer | Number of extracted alternative routes |
| `top_attack_classes` | array | Dominant extracted attack classes |
| `dominant_finding_class` | string | Main finding class assigned for Paper 2 synthesis |
| `first_round_iso` | string or null | First round timestamp when available |
| `last_round_iso` | string or null | Last round timestamp when available |
| `metric_history` | array | Round-level metric history when available |
| `metric_final` | number or null | Final metric value when available |

## `per-campaign-summary.csv`

Format: CSV with one header row and 17 campaign rows.

Columns:

| Column | Description |
|---|---|
| `run_id` | Internal campaign identifier |
| `instrumentation_level` | Instrumentation level used for evidence weighting |
| `n_rounds` | Round count represented for the campaign |
| `dominant_finding_class` | Finding class used in Paper 2 synthesis |
| `terminate_no_route` | Count or binary marker for terminate-no-route outcome |
| `peer_convergence_count` | Count of peer convergence markers |
| `alternative_routes_count` | Number of extracted alternative routes |
| `dominant_attack_class` | Dominant attack class label |
| `key_finding_one_line` | One-line campaign finding summary |

## `anc/attack-registry.jsonl`

Format: JSON Lines, 52 strict-parsed rows.

Per-row fields include:

- `attack_id`;
- `attack_class`;
- `attack_subclass`;
- `attack_header_pattern`;
- `criterion_4_form`;
- `evidence_quote`;
- `peer_file_path`;
- `peer_role`;
- `resolution_status`;
- `round_n`;
- `run_id`;
- `severity`;
- `source_file`;
- `source_line_start`;
- `source_line_end`.

## `anc/recurring-attacks.csv`

Format: CSV.

This file records the post-quarantine recurring attack subclass count. The v0.1.0
copy has one data row plus header.

## `anc/alternative-routes.jsonl`

Format: JSON Lines, 225 rows.

Per-row fields include:

- `route_id`;
- `run_id`;
- `round_n`;
- `peer_role`;
- `mechanism`;
- `blocker_chain`;
- `est_metric_delta_raw`;
- `est_metric_delta_value`;
- `promoted_to_next_round`;
- `ultimate_outcome`;
- `source_file`;
- `source_line_range`.

## `anc/methodology-self-attacks.jsonl`

Format: JSON Lines, 21 rows.

These are Paper 2 R0 self-attacks used to harden the manuscript and release
contract before synthesis.

Fields mirror the attack registry where applicable.

## `anc/quote-bank.jsonl`

Format: JSON Lines, 40 rows.

Per-row fields include:

- `quote_id`;
- `campaign`;
- `category`;
- `context`;
- `peer_role`;
- `quote`;
- `source_file`;
- `source_line_range`.

## `anc/methodology-timeline.md`

Format: Markdown timeline.

This file preserves the methodology timeline extracted from the internal Paper 2
campaign. The release copy preserves the source file as-is for archival
traceability.
