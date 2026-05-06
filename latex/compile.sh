#!/usr/bin/env bash
set -e
echo "==> Compiling main.tex"
pdflatex -interaction=nonstopmode -halt-on-error main.tex || (echo "FIRST PASS FAILED"; cat main.log | tail -30; exit 1)
bibtex main || (echo "BIBTEX FAILED"; cat main.blg | tail -30; exit 1)
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
echo "==> Cleaning intermediate files"
rm -f main.aux main.bbl main.blg main.log main.out main.toc main.run.xml main-blx.bib
echo "==> main.pdf ready"
ls -la main.pdf
