# Context
## Status: Latex project created
[GREEN]

## Contents
1. [Status: Latex project created](#status-latex-project-created)  
2. [Contents](#contents)  
3. [Next steps](#next-steps)  
4. [Questions / Barriers](#questions--barriers)  
	1. [None](#none)  
5. [Completed](#completed)  
6. [How To's](#how-tos)  
	1. [Where can I download the Latex software?](#where-can-i-download-the-latex-software)  
	2. [Where can I find a Latex Reference? (copy/pastable)](#where-can-i-find-a-latex-reference-copypastable)  
		1. [Cheat Sheet](#cheat-sheet)  
		2. [Comprehensive Latex Symbol List](#comprehensive-latex-symbol-list)  
	3. [How do I view the document?](#how-do-i-view-the-document)  
	4. [How to save PDF version of doc?](#how-to-save-pdf-version-of-doc)  
	5. [How do I insert a TOC (for this context doc on Git - Not Latex)?](#how-do-i-insert-a-toc-for-this-context-doc-on-git--not-latex)  
	6. [How do I auto generate TOC for this document (context.md for git)?](#how-do-i-auto-generate-toc-for-this-document-contextmd-for-git)  
7. [TIPS](#tips)  
8. [REFERENCES](#references)  
	1. [Cheat Sheet](#cheat-sheet)  
	2. [Comprehensive Latex Symbol List](#comprehensive-latex-symbol-list)  
	3. [Add simple equations to doc](#add-simple-equations-to-doc)  
	4. [Limits, Summation & Integrals](#limits-summation--integrals)  
	5. [Converting .tex for use on web page](#converting-tex-for-use-on-web-page)  
	6. [Markdown cheat sheet - GIT](#markdown-cheat-sheet--git)  
	7. [GFM - Git Flavoured Markdown](#gfm--git-flavoured-markdown) 


## Next steps
How to embed into a web page - quiz question for example?

## Questions / Barriers
### None


## Completed
2020.Feb.22 - SF - Create Context Template
 - Create Hello Wolrd Latex doc
 - Create equation cheat sheet, added equations w/ the following notations.
Greek symbols, super script, subscript, fraction, n root x, powers, combined super & sub script, matrix w/ fraction,
differentials, product summatiom, integration.


## How To's
### Where can I download the Latex software?
All platforms available from the Latex Project
[https://www.latex-project.org/get/](https://www.latex-project.org/get/)

### Where can I find a Latex Reference? (copy/pastable)
#### Cheat Sheet
[https://www.nyu.edu/projects/beber/files/Chang_LaTeX_sheet.pdf](https://www.nyu.edu/projects/beber/files/Chang_LaTeX_sheet.pdf)  
#### Comprehensive Latex Symbol List
[http://mirror.ox.ac.uk/sites/ctan.org/info/symbols/comprehensive/symbols-a4.pdf](http://mirror.ox.ac.uk/sites/ctan.org/info/symbols/comprehensive/symbols-a4.pdf)

### How do I view the document?
Double click on file_name.tex or open TexShop (installed in step 1) to create a new .tex (and pdf)
Hit the Typeset button TLHC. The Markup is then compiled and (if successful) diaplyed as a PDF.
If not successful the line ref of the error is on the LHS of the editor.

### How to save PDF version of doc?
PDF file is automatically generated when Typset is clicked. It's placed in the same folder as the .tex file.




### How do I insert a TOC (for this context doc on Git - Not Latex)?
To create a link to a chapter in MD:
```
[Text to Display](#text-from-title)\
[Q's & How To's](#qs--how-tos)\
```

The text-from-title is the the text from the title downcased, with spaces replaced with a hyphen '-' and non alphanumeric characters removed. So "Q's & How To's" becomes '#qs--how-tos'
The '\\' at the end of the line is same as <br> or CRLF. (New line)

To create a TOC, create a numbered list of links. Tab in next level with new numbers.
```
1. [Current status](#status)\
2. [Contents](#contents)\
3. [Next steps](#next-steps)\
4. [Completed](#completed)\
5. [Q's & How To's](#qs--how-tos)\
    1. [Adding tabs to content links](#adding-tabs-to-content-links) \
    2. [Auto generaging TOC](#auto-generaging-toc)\
6. [Tips on context doc](#tips)\
7. [References](#references)
```

### How do I auto generate TOC for this document (context.md for git)?
```
$ cd /lang/linux_mix/linux_bike             # cd into repo - same dir as the README.md file
                                            # or context.md file
$ spe                                       # venv for python scrips
                                            # alias spe='. /repos/python_scripts/venv/bin/activate'   
$ [create_TOC_for_md.py]                      # run script
                                            # paste output into .md file TOC
```
Available here: [create_TOC_for_md.py](https://github.com/UnacceptableBehaviour/python_scripts/blob/master/create_TOC_for_md.py)  


## TIPS
Keep status concise:  
Put the colour in square brackets on the next line immediately after status  
RED   - Stalled, technology/cost barrier.  
AMBER - Work in progress.  
GREEN - Complete.  
BLUE  - Parked, no action planned. (maybe incomplete / redundant)  

<br>/CRLF in markdown is endline \\


## REFERENCES
### Cheat Sheet
[https://www.nyu.edu/projects/beber/files/Chang_LaTeX_sheet.pdf](https://www.nyu.edu/projects/beber/files/Chang_LaTeX_sheet.pdf)

### Comprehensive Latex Symbol List
[http://mirror.ox.ac.uk/sites/ctan.org/info/symbols/comprehensive/symbols-a4.pdf](http://mirror.ox.ac.uk/sites/ctan.org/info/symbols/comprehensive/symbols-a4.pdf)

### Add simple equations to doc
https://www.youtube.com/watch?v=1pCdiDin02s

### Limits, Summation & Integrals
https://www.youtube.com/watch?v=c5X7Xj1iYak

### Converting .tex for use on web page
https://tex.stackexchange.com/questions/23804/how-to-incorporate-tex-into-a-website

### Markdown cheat sheet - GIT
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

### GFM - Git Flavoured Markdown
https://github.github.com/gfm/
