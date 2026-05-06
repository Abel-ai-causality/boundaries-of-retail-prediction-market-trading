# Paper 2 LaTeX Package v0.1.0

Overleaf-ready LaTeX package for "Boundaries of Retail Quantitative Trading on Prediction Markets: A Multi-Mechanism Empirical Retrospective."

## Overleaf upload (recommended path)

Visit https://www.overleaf.com, then choose New Project -> Upload Project.

Drag this directory as a zip, or use Overleaf's git integration.

Set Compiler to pdfLaTeX.

Set Main document to `main.tex`.

Use `references.bib` for BibTeX. In Project menu -> Settings, set Compiler = pdfLaTeX.

## Local compile

Prerequisites: TeXLive 2022+ or MacTeX, or MikTeX on Windows.

Run:

```bash
bash compile.sh
```

or:

```bash
make
```

Output: `main.pdf`.

## Repository structure

```text
paper-2-latex/
├── main.tex
├── references.bib
├── compile.sh
├── Makefile
├── README.md
└── main.pdf
```

## Citation

```bibtex
@misc{Wang2026Paper2,
  title = {Boundaries of Retail Quantitative Trading on Prediction Markets: A Multi-Mechanism Empirical Retrospective},
  author = {Stephen Wang},
  year = {2026},
  institution = {Abel AI Lab},
  note = {Working paper}
}
```

## License

Code is Apache-2.0. Documentation is CC BY 4.0.

## Notes

The arXiv submission package is the same content. If arXiv tooling strips `biblatex`, or if `biblatex` with `backend=bibtex` does not work in a target environment, fall back to `natbib` with `\bibliographystyle{unsrt}`.
