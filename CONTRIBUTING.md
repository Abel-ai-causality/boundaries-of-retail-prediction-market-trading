# Contributing

Thank you for helping improve the Paper 2 release package.

This repository is a research artifact. The highest-value contributions are
small, verifiable, and scoped to reproducibility, citation correctness, data
dictionary clarity, or methodology questions grounded in a specific row.

## Report Issues

Use the issue templates in `.github/ISSUE_TEMPLATE/`.

Use `bug-report.md` when something fails to run or a file is missing.

Use `methodology-question.md` when the question concerns a finding, campaign,
quote-bank row, attack-registry row, or interpretation boundary.

Please include:

- repository version or commit SHA;
- operating system and Python version;
- exact command run;
- expected result;
- actual result;
- relevant file path and line if available.

## Propose Changes

Open a pull request with a narrow scope.

Preferred PRs:

- fix one broken link or citation;
- clarify one data field;
- improve one reproduction command;
- correct one typo or stale path;
- add one focused validation check.

Avoid large mixed PRs that combine manuscript edits, data edits, code changes,
and metadata changes. Split them so review can stay mechanical.

## Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The main eval uses Python standard-library modules only. Optional local tools:

- `cffconvert` for validating `CITATION.cff`;
- `markdownlint-cli` for checking Markdown style.

## Testing

Run the paper eval before opening a PR:

```bash
bash code/eval/pm-trading-boundaries-eval.sh
cat .eval/rbaseline-eval.log
```

For manuscript, bibliography, and data changes, the expected release gate is:

```text
paper_readiness_score >= 85
hard_gate_violations=[]
```

Also validate JSON when touching metadata or aggregate data:

```bash
python3 -m json.tool .zenodo.json >/tmp/paper2.zenodo.json
python3 -m json.tool data/cross-campaign-aggregate.json >/tmp/paper2.aggregate.json
```

## Code Style

Python:

- target Python 3.11+;
- follow PEP 8 where practical;
- prefer standard-library modules unless a dependency is justified;
- keep comments short and focused on non-obvious logic.

Markdown:

- use clear headings;
- keep relative links stable;
- avoid changing citation semantics without explaining the evidence;
- run markdown linting when available.

## Citation Policy

Cite Paper 2 when using this retrospective's campaign corpus, data registries,
eval gate, or bounded claims about the observed LLM-assisted trading routes.

Cite MarketAnchor v0.1.2 separately when discussing consensus-anchor sensitivity
in the stored matched-framing benchmark.

Cite the original prior work for general claims about LLM forecasting, anchoring,
market microstructure, prediction markets, or backtest selection bias.

## Conduct

All contributors are expected to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
