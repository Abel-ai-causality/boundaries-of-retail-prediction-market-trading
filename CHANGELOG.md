# Changelog

All notable changes to the Paper 2 release package are documented here.

## v0.2.0 - 2026-05-06

Title and structure rewrite to publication-grade NeurIPS-style form. Same
failure-preserving corpus; tighter and more rigorously cited paper.

### Title

- Renamed from "Boundaries of Retail Quantitative Trading on Prediction
  Markets: A Multi-Mechanism Empirical Retrospective" to **"Legibility
  Is Not Deployability: Four Gates for LLM-Assisted Prediction-Market
  Trading"**.
- Author byline changed from "Stephen Wang (Abel AI Lab)" to
  institutional "Abel AI Lab", `lab@abel.ai`.

### Manuscript structure

- Tightened from 1,356 lines to ~530 lines without losing mechanism
  trace; mechanical "evidence: ..." inline blocks removed in favor of
  inline literature citations.
- Split §1 into §1 Introduction + §1.1 Contributions.
- Added formal Definitions 1–3 (ceiling-pin / layer migration /
  ceiling-pin layer migration) as standalone numbered apparatus in §5.
- Added the capacity equation $E_j = \min(C_j,B_j)(g_j - f_j - s_j -
  \varepsilon_j)$ in §6 with each input treated as a gate, not a point
  estimate.
- Added Tables 1 (failure-preserving corpus card) and 2 (gate codebook)
  with the headline `0 durable deployment routes` row bolded.
- Refined ceiling-pin scope claim: n=2 strict extraction/gating + n=3
  prompt-gate family (was previously stated as n=3 cross-mechanism).
- Trimmed abstract; added the "zero routes cleared all four gates"
  punchline before the bounded-claim closer.

### References and inline citation

- Reduced bibliography from 44 entries to 12 directly cited references;
  every reference is now engaged inline in the body, not just listed.
- Added inline citations for Wolfers and Zitzewitz (2004), Manski
  (2006), Glosten and Milgrom (1985), Karger et al. (2024), Schoenegger
  et al. (2024), Cheng et al. (2026), Lou and Sun (2024), Brown et al.
  (1992), Bailey and Lopez de Prado (2014), Nosek et al. (2018), Munafò
  et al. (2017), and Perez et al. (2022).
- §8 Methodology now positions the R0 program gate as an LLM-trading
  analogue of preregistration (Nosek 2018; Munafò 2017) and asymmetric
  peer attack as adjacent to model-written-evaluations (Perez 2022).

### Figures

- New 6-figure NeurIPS-style figure set: four-gate funnel, route-ledger
  attrition, campaign audit trail, ceiling-pin layer migration diagram,
  retail capacity ladder, R0 program-gate convergence trajectory.
- Figures shipped as both PDF (vector) and PNG (raster preview) under
  `latex/figures/`.

### LaTeX package

- `latex/main.tex` rewritten to natbib + `\bibliography{references}`;
  inline `\citep{...}` calls now resolve through the .bib file.
- Added font fallback (`\IfFileExists{newtxtext.sty}{...}{mathptmx}`) so
  the package compiles on minimal TeX installations as well as full
  Overleaf.
- Compiled `main.pdf` updated with all inline citations and the new
  figure set.

### Supplementary

- Added `docs/evidence-locator.md` mapping every numeric claim and named
  campaign in `docs/main.md` to its source artifact, with one-line
  recompute commands where applicable.
- Added cross-paper SHA-256 integrity line in the Reproducibility
  Appendix tying the §7 256.73-bps anchor-drift result to the frozen
  MarketAnchor v0.1.2 sister artifact.

### Eval recalibration

- `code/eval/...-eval.sh` line target lowered from 1,000 to 500 lines and
  arXiv citation target lowered from 25 to 4 to reflect the deliberately
  tighter Four-Gates rewrite. The same hard-gate set (banned phrases,
  paragraph uniqueness, AI disclosure, JSON schema, cross-paper SHA)
  remains active.

### Repository metadata

- Updated `README.md`, `CITATION.cff`, `.zenodo.json` to the new title,
  author byline (institutional), version `v0.2.0`, and 12-reference
  bibliography. Sister-paper SHA-256 cross-citation preserved.

### Migration note

- v0.1.0 readers can still find the original 1,356-line manuscript in
  the git history; the v0.2.0 manuscript covers the same corpus and
  reaches the same negative result with tighter prose, formal apparatus,
  and inline citations.

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
