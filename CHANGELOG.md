# Changelog

All notable changes to the Paper 2 release package are documented here.

## v0.1.0 - 2026-05-06

Initial public-release preparation after the internal Abelian campaign.

### R0 Gate

- Established the Paper 2 retrospective program contract.
- Ran initial peer challenge on scope, section count, evidence targets, and
  reproducibility criteria.
- Recorded 21 Paper 2 methodology self-attacks.
- Used the R0 gate to prevent premature release before the evidence package was
  internally consistent.

### R1 Corpus Extraction

- Extracted cross-campaign inventory from the internal Abelian runs.
- Produced the 17-row cross-campaign aggregate JSON.
- Produced the 17-row per-campaign CSV summary.
- Strict-parsed 52 attack rows into the attack registry.
- Built the 225-row alternative-route registry.
- Built the 40-row quote bank.

### R2 Synthesis

- Drafted the manuscript around four bounded findings:
  math-arbitrage saturation, LLM-extraction ceiling-pin behavior,
  retail-bankroll capacity limits, and anchoring uncertainty.
- Added the MarketAnchor v0.1.2 sister-paper bridge.
- Added AI/tool assistance disclosure and reproducibility appendix.
- R2 included padding pressure that was later cleaned up instead of retained.

### R3 Padding Cleanup

- Removed repetitive or low-information paragraphs.
- Preserved line-count readiness through substantive content rather than filler.
- Kept the hard gate against low paragraph uniqueness.
- Maintained zero banned-phrase hits.

### R4 Substantive Expansion

- Expanded the related-work, methodology, limitations, and open-problem sections.
- Clarified single-lab and single-period scope.
- Marked the n=3 ceiling-pin evidence as suggestive.
- Added stronger distinctions between trading PnL, anchor drift, calibration,
  and expected return.

### Polish

- Smoothed manuscript structure and citation language.
- Preserved exact artifact paths in the reproducibility appendix.
- Added release-local repository files for GitHub review.
- Prepared dual-license placeholders pending Abel AI Lab confirmation.

### RW-Canonical References

- Consolidated the 44-entry BibTeX bibliography.
- Verified 32 arXiv IDs against the paper.
- Removed unverified citation extras from the manuscript eval.
- Preserved MarketAnchor v0.1.2 as citation pending until an external identifier
  exists.

### Release Package

- Added `README.md`, `CITATION.cff`, `.zenodo.json`, issue templates, pull
  request template, and GitHub Actions workflows.
- Copied the manuscript, bibliography, retrospective companion doc, sister paper,
  data registries, eval shell, and Path C engineering primitives into the
  release tree.
- Made the copied eval shell locate release-local paths instead of private
  workspace paths.

### Scope Notes

- This is an initial public-release package.
- It is not a trading system and does not include production execution code.
- The evidence remains a single-lab, single-period retrospective.
- Stephen Wang must confirm code, docs, and data license choices before public
  push.

### Future

- MarketAnchor v0.2 sister work with broader anchor controls.
- Multi-lab or independent replication of ceiling-pin behavior.
- Smart-money signal program focused on participant behavior rather than LLM
  narration.
- Stronger external DOI and arXiv metadata once public release identifiers exist.
