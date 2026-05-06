.PHONY: all clean

all: main.pdf

main.pdf: main.tex references.bib
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	bibtex main
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.toc main.run.xml main-blx.bib

distclean: clean
	rm -f main.pdf
