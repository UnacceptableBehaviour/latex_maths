Maths - Brush up list
file:/a_syllabus/_COURSES_00_WIP/MATHS_00_MIT_6.042.rtf
REPO: 

Abstract
Maths revision & learning

## Contents  
1. [AIM:](#aim)  
2. [Asymptotic Notation](#asymptotic-notation)  
	1. [References](#references)  
3. [Recurrence resolution for - Algos L3 34m](#recurrence-resolution-for--algos-l3-34m)  
	1. [References](#references)  
4. [Another topic](#another-topic)  
	1. [References](#references)  
5. [How To s](#how-to-s)  
	1. [Where are Latex Examples for this repo?](#where-are-latex-examples-for-this-repo)  
	2. [How to setup autogenerate README.md file from RTF notes?](#how-to-setup-autogenerate-readmemd-file-from-rtf-notes)  
	3. [How do I autogenerate README.md file from RTF?](#how-do-i-autogenerate-readmemd-file-from-rtf)  
	4. [How can I add maths formulas to README.md?](#how-can-i-add-maths-formulas-to-readmemd)  
		1. [Manually: Generate math image and embed it.](#manually-generate-math-image-and-embed-it)  
		2. [Automagically: Install texify.](#automagically-install-texify)  
6. [References](#references)  


## AIM:  

Maths needs to be good enough to support Algorithms






- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Asymptotic Notation

6.04J Intro Algorithms L2: Asymptotic Notation | Recurrences | Substitution, Master Method ()  

6.042 2010 - L12 -  Sums ()  

6.042 2010 - L13 -  Sums & Asymptotics ()  



### References
6.042 L13 Asymptotic Notation Problems


6.042 L13 Asymptotic Notation Above Problems w/ Solutions



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Recurrence resolution for - Algos L3 34m 

Recurrence is basically a computable sequence set out from a set of start rules and a base case.  
  
EG Fibonacci: first two numbers are 0 and 1 the rest are defined as the the sum of the two preceding numbers  
0	1	1	2	3	5	8	13	.	. 	you get it  

formally defined:
$$
\begin{equation}
  a_n = a_{n-1} + a_{n-2}
\end{equation}
\begin{equation}
  n \geq 2
\end{equation}
\begin{equation}
  a_0 = 0
\end{equation}
\begin{equation}
  a_1 = 1
\end{equation}
$$

[Recurrence Relations - Discrete Maths](https://www.youtube.com/watch?v=eAaP4XaB8hM)   

$$
\begin{equation}
  a_n - a_{n-1} = k
\end{equation}
\begin{equation}
  a_0 = c
\end{equation}
$$

Thats to say where the difference between one element in the sequence and the next is constant (k in this equation) and the base case is c the following holds:  
$$
\begin{equation}
  a_n = c + \sum_{i=1}^{n}k
\end{equation}
$$

Note: (summation proof @ 14m)
$$
\begin{equation}
  \sum_{i=1}^{n}i = \frac{n(n+1)}{2}
\end{equation}
$$









### References
[Recurrence Relations - Discrete Maths](https://www.youtube.com/watch?v=eAaP4XaB8hM)   

Sumation proof @ 14m



[Discrete Mathematics] Nonhomogeneous Recurrence Relations


[Solving Recurrence Relations](https://www.youtube.com/watch?v=7mhvA5L7KqY)  


[6.042 pdf notes - recurrences](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap10.pdf)  


[basic Proof by induction](https://www.youtube.com/watch?v=t_3ACuzEe_8)  




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -






- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Another topic




### References
Limits algebra - manipulations and rules.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## How To s
### Where are Latex Examples for this repo?
[Example equations in PDF format](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/hello_world.pdf)  
This pdf doc is generated using TeXShop from [hello_world.tex](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/hello_world.tex)  


### How to setup autogenerate README.md file from RTF notes?
```
> python --version			# Python 2.7.16
> python3 -m venv venv
> .pe					# alias .pe='. venv/bin/activate'
> python --version			# Python 3.7.5
> pip install --upgrade pip
> pip install striprtf			# for rtf processing
```

### How do I autogenerate README.md file from RTF?
```
> .pe				# alias .pe='. venv/bin/activate'
> ./create_TOC_for_md.py -p	# takes MATHS_00_MIT_6.042.rtf course notes and add TOC > README.md
				# also add README.md to git, commits, and pushes
				# -p = commit & push
```

### How can I add maths formulas to README.md?
#### Manually: Generate math image and embed it.
Install Latex tools [notes here](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/context.md)  
Open LaTeXit edit equation click text and hit the LaTeXit button to check its good.  
Export as png and upload it to git (need to do this so the URL and be used to embed the image)  
Embed image with  
```
![uses dot product of the vector of each document](https://github.com/UnacceptableBehaviour/algorithms/blob/master/formulae/20200228_1715_dot_prod_doc_distance.png)  
Note the ! before opening [ denotes image
```
#### Automagically: Install texify.
[Find texify here](https://github.com/agurodriguez/github-texify)  
Use LaTeXit to check formula correctness then past it into doc surrounded by consecutive \$ symbols like so
![latex script](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/images/latex_example.png)  

Will display the following document distance equation  
$$
\begin{equation}
  D_1.D_2\\
\end{equation}
\begin{equation}
  \sum_{w}D_1[w].D_2[w]
  \label{sum}  
\end{equation}
$$



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## References
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Courses / Books Found w/ Summary:

Prerequisite: Maths for CS: 
2015 https://www.youtube.com/watch?v=wIq4CssPoO0&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ  
	[L3.2.1 Asymptotic Notation] (https://www.youtube.com/watch?v=CWkh5kb4TGc&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ&index=72)  
	[L 3.2.3 Asymptotic Properties] (https://www.youtube.com/watch?v=HeyEK0TWiBw&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ&index=73)  
	[L 3.2.6 Asymptotic Blunder inc Big O] (https://www.youtube.com/watch?v=Y9Blo_G-Mvg&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ&index=74)  
2010 https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/  
	[L12 Sums] (https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/lecture-12-sums/)  
	[L12 Sums and Asymptotics] (https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/lecture-13-sums-and-asymptotics/)  

Topics: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/  
Prerequisite: Probability: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-spring-2006/   
Assignments w solutions: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-spring-2006/assignments/    

