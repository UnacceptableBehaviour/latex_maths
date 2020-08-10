Maths - Brush up list
file:/a_syllabus/_COURSES_00_WIP/MATHS_00_MIT_6.042.rtf
REPO: 

Abstract
Maths revision & learning 
[MIT 6.042J](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/syllabus/)  

## Contents  
1. [AIM:](#aim)  
2. [Logarithms - identities & basic manipulation](#logarithms---identities--basic-manipulation)  
		1. [Identities](#identities)  
		2. [Practice questions](#practice-questions)  
	1. [References](#references)  
3. [Asymptotic Notation](#asymptotic-notation)  
	1. [6.042 2010 - L12 -  Sums](#6042-2010---l12----sums)  
		1. [Vid contents](#vid-contents)  
	2. [Problems](#problems)  
	3. [6.042 2010 - L13 -  Sums & Asymptotics](#6042-2010---l13----sums--asymptotics)  
		1. [Vid contents](#vid-contents)  
		2. [Notes](#notes)  
		3. [References](#references)  
	4. [6.042 2010 - L14 -  Divide and Conquer Recurrences](#6042-2010---l14----divide-and-conquer-recurrences)  
		1. [Vid contents](#vid-contents)  
		2. [Notes](#notes)  
		3. [References](#references)  
	5. [6.042 2010 - L15 - Linear recurrence](#6042-2010---l15---linear-recurrence)  
		1. [Vid contents](#vid-contents)  
		2. [Notes](#notes)  
		3. [References](#references)  
	6. [6.04J Intro Algorithms L2: Asymptotic Notation | Recurrences | Substitution, Master Method ()](#604j-intro-algorithms-l2-asymptotic-notation--recurrences--substitution-master-method-)  
4. [Recurrence resolution for - Algos L3 34m](#recurrence-resolution-for---algos-l3-34m)  
	1. [Problems](#problems)  
	2. [References](#references)  
5. [Python - matplotlib, numpy](#python---matplotlib-numpy)  
	1. [How so I plot a chart with python?](#how-so-i-plot-a-chart-with-python)  
	2. [How do I save that chart to disk?](#how-do-i-save-that-chart-to-disk)  
	3. [How Do I invert x axis?](#how-do-i-invert-x-axis)  
	4. [References](#references)  
6. [Another topic](#another-topic)  
	1. [References](#references)  
7. [Glossary / Vocab](#glossary--vocab)  
8. [How To s](#how-to-s)  
	1. [Where are Latex Examples for this repo?](#where-are-latex-examples-for-this-repo)  
	2. [How to setup autogenerate README.md file from RTF notes?](#how-to-setup-autogenerate-readmemd-file-from-rtf-notes)  
	3. [How do I autogenerate README.md file from RTF?](#how-do-i-autogenerate-readmemd-file-from-rtf)  
	4. [How can I add maths formulas to README.md?](#how-can-i-add-maths-formulas-to-readmemd)  
		1. [Manually: Generate math image and embed it.](#manually-generate-math-image-and-embed-it)  
		2. [Automagically: Install texify.](#automagically-install-texify)  
9. [References](#references)  


## AIM:  

Maths needs to be good enough to support MIT Algorithms course  

Sometimes an equation is unintelligible due to lack of vocabulary / symbol knowledge!!  

A good place to start in this case is wikipedias [List of mathematical symbols by subject](https://en.wikipedia.org/wiki/List_of_mathematical_symbols_by_subject)  
A less intimidating list of [symbols by subject inc greek symbols](https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html#calculus)  
Good to know your [Greek symbols & Latex cheat sheet pdf](http://wch.github.io/latexsheet/latexsheet-a4.pdf)  
Latex [full reference](http://www.icl.utk.edu/~mgates3/docs/latex.pdf)  
Maths on [git](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/context.md)





[MIT 6.042J Mathematics for Computer Science, Fall 2010 - Video](https://www.youtube.com/watch?v=L3LMbpZIKhQ&list=PLB7540DEDD482705B)  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Logarithms - identities & basic manipulation

#### Identities  
[Good plain resource identities w/ examples](https://courses.cs.washington.edu/courses/cse373/19sp/resources/math/exponents-and-logs/) Logarithmic [identities:](https://en.wikipedia.org/wiki/List_of_logarithmic_identities)  

Relationship between power, root & log:  
\begin{equation}
   \mbox{given }\hspace{10pt}x^y = z \hspace{30pt} log_x(z) = y \hspace{30pt} \sqrt[y]{z} = x
\end{equation}
\begin{equation}
   \mbox{ inverse operations } 
\end{equation}
\begin{equation}
     x^{log_x(z)} = z \hspace{30pt} log_x(x^y) = y
\end{equation}
\begin{equation}
     log_{\sqrt[y]{z}}(z) = y \hspace{30pt} \sqrt[log_x(z)]{z} = x
\end{equation}
\begin{equation}
     \sqrt[y]{x^y} = x \hspace{30pt} (\sqrt[y]{z})^y = z
\end{equation}

Interesting notation and [video on how the 3 relate - and triangle notation](https://www.youtube.com/watch?v=sULa9Lc4pck)

#### Practice questions
1. [Tests Q s - Pauls Online Notes](https://tutorial.math.lamar.edu/Problems/Alg/SolveLogEqns.aspx) refresher DONE  
2. [Q s log & exponential quiz qs from studywell.com](https://studywell.com/wp-content/uploads/2018/03/SolomonLogRulesQuestions.pdf) and [Answers](https://studywell.com/wp-content/uploads/2018/03/SolomonLogRulesSolutions.pdf) TODO  


### References
Logarithmic identities  
https://en.wikipedia.org/wiki/List_of_logarithmic_identities

Good plain resource identities w/ examples  
https://courses.cs.washington.edu/courses/cse373/19sp/resources/math/exponents-and-logs/

Washington Edu  
https://courses.cs.washington.edu/courses/cse373/19sp/resources/

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -





- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Asymptotic Notation

### 6.042 2010 - L12 -  Sums   
[vid](https://www.youtube.com/watch?v=fAeShezAGLE) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap09.pdf) ~ 
Code: 
Reading: [C9 Sums & Asymptotics](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap09.pdf)  

List of [Summation identities!](https://en.wikipedia.org/wiki/Summation)    

#### Vid contents
0-18m annuity equation  
9m50 total current value of an n year annuity of annual value mUSD  
12m Following reads for all n greater than equal to 1 where x not eq 1 sum . . . CLOSED FORM proved by induction  
\begin{equation}
    \forall n\geq1, x\ne1, \;\;  \sum_{i=0}^{n-1} x^i = \frac{1-x^n}{1-x}
\end{equation}
12m Reaching CLOSED FORM expression for annuity by substituting into CLOSED FROM series just derived.  
18m30 How mush is 50K for eternity?  - Spoiler: USD50K for eternity @ p=0.06 comes in @ USD883,333  
21m40   series - where - getting closed form formulas   
21m50 Sum to infinity of x^i wher x<1  
\begin{equation}
    if |x|<1,\;  \sum_{i=0}^{\infty} x^i = \frac{1}{1-x}
\end{equation}
24m  SUM ix^i  - formula 27m40  
28m30 DERIVATIVE method  
32m taking the derivative TWICE to solve the homework   
34m evaluating a company based on anual growth - similar to annuity maths  <<< USEFUL!!!   
40m SUM i2^-i  
42m proof by induction of  
\begin{equation}
  \sum_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6}
\end{equation}
42m proof by induction of  


NEXT - add rest of timing continue notes from 20m

**Notes on lecture**  
Annuity - pays a fixed amount of value every years **(m)** for a number of years **(n)**  
Q: you want EU50000 a year for 20 years of EU1M today or EU700K today or EU500K ?  
Calculating value of annuity (shown 1m - 9m48):  
$$
\begin{equation}
  V = \sum_{i=0}^{n-1} \frac{m}{{(1+p)}^i}
\end{equation}
\begin{equation}
    = m\sum_{i=0}^{n-1} x^i  \;\;where\;x=\frac{1}{(1+p)}
\end{equation}
$$



Using perturbation method to prove:  
\begin{equation}
    \sum_{i=0}^{n-1} x^i = \frac{1-x^n}{1-x}
\end{equation}
\begin{equation}
    S = 1 + x +x^2 +x^3 +x^{n-1}
\end{equation}
seriex S * x
\begin{equation}
   xS = \;\; x +x^2 +x^3 +x^{n-1} +x^n
\end{equation}
subtracting xS from S
\begin{equation}
   (1-x)S = 1 - x^n
\end{equation}
leaving
\begin{equation}
   S = \frac{1 - x^n}{1-x}
\end{equation}
So
\begin{equation}
    \forall n\geq1, x\ne1, \;\;  \sum_{i=0}^{n-1} x^i = \frac{1-x^n}{1-x} = S
\end{equation}
\begin{equation}
  V = \sum_{i=0}^{n-1} \frac{m}{{(1+p)}^i}
\end{equation}
\begin{equation}
  V = m\sum_{i=0}^{n-1} \frac{1}{{(1+p)}^i}, \;subs\; \frac{1}{(1+p)}=x 
\end{equation}
\begin{equation}
  V = m\sum_{i=0}^{n-1} x^i, \;or\; V = mS \; and \; S = \frac{1 - x^n}{1-x}
\end{equation}
\begin{equation}
  V = m\left( \frac{1 - x^n}{1-x} \right) \;subs\;x=\frac{1}{(1+p)}
\end{equation}
\begin{equation}
  V = m\left( \frac{1 - \left({\frac{1}{(1+p)}}\right)^n}{1-{\frac{1}{(1+p)}}} \right)
\end{equation}
\begin{equation}
  1-{\frac{1}{(1+p)}} = \frac{(1+p)}{(1+p)}-\frac{1}{(1+p)} = \frac{p}{(1+p)}
\end{equation}
\begin{equation}
  V = m\left( \frac{1 + p - \frac{1}{(1+p)^{n-1}}}{p} \right)
\end{equation}
Where  
m - payment every year  
p - interest rate  
n - number of years  
  
Note - payments for ever (to infinity) example  
\begin{equation}
  if\;n=\infty, \; V = m\left( \frac{1 + p}{p} \right)\; since\; lim_{n\to\infty}\frac{1}{(1+p)^{n-1}}\rightarrow0
\end{equation}
So for m=USD50K, p=0.06 V=USD883,333

\begin{equation}
   \mbox{absolute }|x| < 1  \mbox{  when } n \to \infty
\end{equation}
\begin{equation}
   x^n \to 0  \mbox{  since } x < 1,  x^n\;becomes\;minuscule\;tending\;to\;0}
\end{equation}
\begin{equation}
   \mbox{so } S = \frac{1}{1-x}
\end{equation}

24m
\begin{equation}
  \mbox{if } |x| < 1 \mbox{, } \sum_{i=1}^{\infty}ix^i = \frac{x}{{(1-x)}^2}
\end{equation}


42m
\begin{equation}
  \sum_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6}
\end{equation}
Proof by induction guess is comes out cubic
\begin{equation}
  \forall n \mbox{, } \sum_{i=1}^{n}i^2 = an^3 + bn^2 + cn + d 
\end{equation}
\begin{multline}
  \begin{matrix}
  n=0 \mbox{, } \Rightarrow 0 = d \\
  n=1 \mbox{, } \Rightarrow 1 = a + b + c + d \\
  n=2 \mbox{, } \Rightarrow 5 = 8a + 4b + 2c + d \\
  n=3 \mbox{, } \Rightarrow 14 = 27a + 9b + 3c + d \\
  \end{matrix}
\end{multline}


### Problems
6.042 L13 Asymptotic Notation Problems


6.042 L13 Asymptotic Notation Above Problems w/ Solutions




### 6.042 2010 - L13 -  Sums & Asymptotics 
[vid](https://www.youtube.com/watch?v=X9eErxRjQEI) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap09.pdf) ~ 
[Problems](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec13.pdf) ~ 
[Solutions](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec13_sol.pdf) ~ 
Reading:

#### Vid contents
TODO

#### Notes

#### References

### 6.042 2010 - L14 -  Divide and Conquer Recurrences
[vid](https://www.youtube.com/watch?v=Kqf0uO0oV6s) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap10.pdf) ~ 
[Problems]() ~ 
[Solutions]() ~ 
Reading:

#### Vid contents
TODO

#### Notes

#### References


### 6.042 2010 - L15 - Linear recurrence
[vid](https://www.youtube.com/watch?v=TWBB-JlmYUc) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap10.pdf) ~ 
[Problems](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec14.pdf) ~ 
[Solutions](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec14_sol.pdf) ~ 
Reading:

#### Vid contents
TODO

#### Notes

#### References
[Discrete Mathematics] Homogeneous Recurrence Relations 25m 


Solving Divide and Conquer Recurrences 22m - Ref to Text book  


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
### 6.04J Intro Algorithms L2: Asymptotic Notation | Recurrences | Substitution, Master Method ()  
	move this to algo repo no?
	Solving Recurrences
	16:50 | 1: Substitution Method
	37:45 | 2: Recursion-tree Method		<<
	48:40 | 3: Master Method



## Recurrence resolution for - Algos L3 34m 
[MIT Recurrences - C10](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap10.pdf)  

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

[Recurrence Relations](https://www.youtube.com/watch?v=eAaP4XaB8hM) Discrete Mathematics 15m   
Also see p303 MIT Recurrences - C10  

In an example series: 0	2	6	12	20	30  
Where the difference between element is 2n  
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



### Problems



### References
[Recurrence Relations - Discrete Maths](https://www.youtube.com/watch?v=eAaP4XaB8hM)   

Sumation proof @ 14m

[Discrete Mathematics] Nonhomogeneous Recurrence Relations


[Solving Recurrence Relations](https://www.youtube.com/watch?v=7mhvA5L7KqY)  


[6.042 pdf notes - recurrences](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap10.pdf)  


[basic Proof by induction](https://www.youtube.com/watch?v=t_3ACuzEe_8)  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Python - matplotlib, numpy
### How so I plot a chart with python?
```
> .pe						# alias .pe='. venv/bin/activate'
> pip install matplotlib			# plotting lib
> pip install numpy				# math sci lib 
> ./matplotlib/plot.py				# super basic 2d plot example
```
[./matplotlib/plot.py](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/matplotlib/plot.py)  
3d plots - [tutorial](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html)  

### How do I save that chart to disk?
Simplest way is to click the disk icon on the display and save to the appropriate place.
Follow instructions to generate chart: [How so I plot a chart with python?](#how-so-i-plot-a-chart-with-python)  
From the code:  
```
> pip install pillow								# support jpg
import matplotlib.pyplot as plt 						# follow ab
plt.plot(elements, zero_2pow_zero, label="Limits n^n n->0 (zero ^ zero)")	# create chart
plt.savefig('matplot_graph.jpg')						# save chart
```
Example : ) 
![matplot_graph.jpg](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/matplotlib/images/matplot_graph.jpg)  

### How Do I invert x axis?
```
import matplotlib.pyplot as plt 						# follow ab
plt.plot(elements, zero_2pow_zero, label="Limits n^n n->0 (zero ^ zero)")	# create chart
plt.gca().invert_xaxis()				# INVERT axis or invert_yaxis()
```



### References
Matplotlib 

Matplotlib - Examples

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -





- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Another topic




### References
Limits algebra - manipulations and rules.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Glossary / Vocab

Proof by Induction		Show base case, show a step, then show formula holds for step +1, and 
Perturbation Method		Take a series pertubing it - by multiplying it for example - solve simultaneous equation


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

