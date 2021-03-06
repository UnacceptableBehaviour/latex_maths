## Maths - Brush up list
file:/a_syllabus/_COURSES_00_WIP/MATHS_00_MIT_6.042.rtf
REPO: 

## Abstract  
Maths revision & learning 
[MIT 6.042J](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/syllabus/)  

## Contents  
1. [Abstract](#abstract)  
2. [Contents](#contents)  
3. [AIM:](#aim)  
4. [Logarithms - identities & basic manipulation](#logarithms---identities--basic-manipulation)  
		1. [Identities](#identities)  
		2. [Practice questions](#practice-questions)  
	1. [References](#references)  
5. [Asymptotic Notation](#asymptotic-notation)  
	1. [6.042 2010 - L12 -  Sums](#6042-2010---l12----sums)  
		1. [**Vid contents**](#vid-contents)  
	2. [6.042 2010 - R12 -  Sums & Asymptotics](#6042-2010---r12----sums--asymptotics)  
		1. [1 The L-tower problem](#1-the-l-tower-problem)  
		2. [2 Double Sums](#2-double-sums)  
	3. [6.042 2010 - L13 -  Sums & Asymptotics](#6042-2010---l13----sums--asymptotics)  
		1. [Vid contents](#vid-contents)  
		2. [Notes](#notes)  
	4. [Problems](#problems)  
		1. [References](#references)  
	5. [6.042 2010 - L14 -  Divide and Conquer Recurrences](#6042-2010---l14----divide-and-conquer-recurrences)  
		1. [Vid contents](#vid-contents)  
		2. [Notes](#notes)  
		3. [References](#references)  
	6. [6.042 2010 - L15 - Linear recurrence](#6042-2010---l15---linear-recurrence)  
		1. [Vid contents](#vid-contents)  
		2. [Notes](#notes)  
		3. [References](#references)  
	7. [6.04J Intro Algorithms L2: Asymptotic Notation | Recurrences | Substitution, Master Method ()](#604j-intro-algorithms-l2-asymptotic-notation--recurrences--substitution-master-method-)  
6. [Recurrence resolution for - Algos L3 34m](#recurrence-resolution-for---algos-l3-34m)  
	1. [Problems](#problems)  
	2. [References](#references)  
7. [Python - matplotlib, numpy](#python---matplotlib-numpy)  
	1. [How so I plot a chart with python?](#how-so-i-plot-a-chart-with-python)  
	2. [How do I save that chart to disk?](#how-do-i-save-that-chart-to-disk)  
	3. [How Do I invert x axis?](#how-do-i-invert-x-axis)  
	4. [References](#references)  
8. [Another topic](#another-topic)  
	1. [References](#references)  
9. [Glossary / Vocab](#glossary--vocab)  
10. [How To s](#how-to-s)  
	1. [Where are Latex Examples for this repo?](#where-are-latex-examples-for-this-repo)  
	2. [How to setup autogenerate README.md file from RTF notes?](#how-to-setup-autogenerate-readmemd-file-from-rtf-notes)  
	3. [How do I autogenerate README.md file from RTF?](#how-do-i-autogenerate-readmemd-file-from-rtf)  
	4. [How can I add maths formulas to README.md?](#how-can-i-add-maths-formulas-to-readmemd)  
		1. [Manually: Generate math image and embed it.](#manually-generate-math-image-and-embed-it)  
		2. [Automagically: Install texify.](#automagically-install-texify)  
11. [References](#references)  


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
<p align="center"><img src="/tex/512c8610141af92f2621de5dd0301d67.svg?invert_in_darkmode&sanitize=true" align=middle width=520.9960222499999pt height=17.4097869pt/></p>
<p align="center"><img src="/tex/49dcd5642097d1b56965fd9484c0f07c.svg?invert_in_darkmode&sanitize=true" align=middle width=414.65764724999997pt height=16.438356pt/></p>
<p align="center"><img src="/tex/4433ead9ede1b782e996181c72cd26c6.svg?invert_in_darkmode&sanitize=true" align=middle width=460.7668642499999pt height=19.526994300000002pt/></p>
<p align="center"><img src="/tex/7fa3f8b9c941502d49a66573bee92f57.svg?invert_in_darkmode&sanitize=true" align=middle width=464.88495735000004pt height=19.703826449999998pt/></p>
<p align="center"><img src="/tex/99ae4551780e4c63110cb7fc125f132e.svg?invert_in_darkmode&sanitize=true" align=middle width=442.46762999999993pt height=18.72257805pt/></p>

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



#### **Vid contents**
0-18m annuity equation  
9m50 total current value of an n year annuity of annual value mUSD  
12m Following reads for all n greater than equal to 1 where x not eq 1 sum . . . CLOSED FORM proved by induction  
<p align="center"><img src="/tex/5db431ab4b10a590ebadc3a10be5397e.svg?invert_in_darkmode&sanitize=true" align=middle width=463.88098679999996pt height=47.35857885pt/></p>  
  
12m Reaching CLOSED FORM expression for annuity by substituting into CLOSED FROM series just derived.  
18m30 How mush is 50K for eternity?  - Spoiler: USD50K for eternity @ p=0.06 comes in @ USD883,333  
21m40   series - where - getting closed form formulas   
21m50 Sum to infinity of x^i wher x<1  
<p align="center"><img src="/tex/f20ccca5edaa03e256009f88d85c3a03.svg?invert_in_darkmode&sanitize=true" align=middle width=440.60539709999995pt height=44.89738935pt/></p>
  
GEOMETRIC SERIES  
24m  PERTURBATION method - SUM ix^i  - formula 27m40 - flesh out notes - add hash for contents  
28m30 DERIVATIVE method - flesh out notes - add hash for contents  
32m taking the derivative TWICE to solve the homework   
34m evaluating a company based on anual growth - similar to annuity maths  <<< USEFUL!!!   
40m SUM i2^-i - write up example - show it  
42m proof by induction of  
<p align="center"><img src="/tex/c70c4bf439e6afaca97c35c4c1880d56.svg?invert_in_darkmode&sanitize=true" align=middle width=442.8349695pt height=44.89738935pt/></p>
42m proof by induction of  
45m tips on guessing solutions and solving simultaneous equation to get CLOSED FOR solution
46m-55m50 - Getting close bounds on a summation series - Integration bounds
55m50 - Example of above when f() increasing - Note formula - on test
1h1m - Definition of tild ~ EG g(x) ~ h(x)
<p align="center"><img src="/tex/85ba7145654529e373f4161b9f4d3b10.svg?invert_in_darkmode&sanitize=true" align=middle width=475.6890831pt height=38.83491479999999pt/></p>
1h7m - Example of above when f() decreasing
1h12m - Symetric upper/lower bound definition - Note formula - on test


NEXT - add rest of timing continue notes from 40m - add maths for red high lights for easy revision

**Notes on lecture**  
Annuity - pays a fixed amount of value every years **(m)** for a number of years **(n)**  
Q: you want EU50000 a year for 20 years of EU1M today or EU700K today or EU500K ?  
Calculating value of annuity (shown 1m - 9m48):  
<p align="center"><img src="/tex/177f113e0b6e80337d8c1599c855a813.svg?invert_in_darkmode&sanitize=true" align=middle width=460.27190385pt height=109.51167315pt/></p>



Using perturbation method to prove:  
<p align="center"><img src="/tex/ebb1fb3b12e0db54ec05421b54d91843.svg?invert_in_darkmode&sanitize=true" align=middle width=407.67503370000003pt height=47.35857885pt/></p>
<p align="center"><img src="/tex/70db5002927e8773cea3f19923881725.svg?invert_in_darkmode&sanitize=true" align=middle width=449.95308270000004pt height=18.312383099999998pt/></p>
seriex S * x
<p align="center"><img src="/tex/6566433c79482260ec6861bc8c2202d6.svg?invert_in_darkmode&sanitize=true" align=middle width=464.27852624999997pt height=18.312383099999998pt/></p>
subtracting xS from S
<p align="center"><img src="/tex/92ce160ae3d15e5d3514605a50da4be3.svg?invert_in_darkmode&sanitize=true" align=middle width=415.18152884999995pt height=16.438356pt/></p>
leaving
<p align="center"><img src="/tex/214cd0f36be857955d171a3e1fdb7c7e.svg?invert_in_darkmode&sanitize=true" align=middle width=391.90872435pt height=34.68611685pt/></p>
So
<p align="center"><img src="/tex/2ae9584d05cf1df660625d9aedf94d9c.svg?invert_in_darkmode&sanitize=true" align=middle width=480.35348129999994pt height=47.35857885pt/></p>
<p align="center"><img src="/tex/41dffa9c88a19027368cfaa3ad902b44.svg?invert_in_darkmode&sanitize=true" align=middle width=410.95510335pt height=47.35857885pt/></p>
<p align="center"><img src="/tex/1de33f092a52ed0377db1f39071677d8.svg?invert_in_darkmode&sanitize=true" align=middle width=486.01058715pt height=47.35857885pt/></p>
<p align="center"><img src="/tex/bd6e772e7c871c9e2c3499231af4add3.svg?invert_in_darkmode&sanitize=true" align=middle width=503.9265792pt height=47.35857885pt/></p>
<p align="center"><img src="/tex/7952effa4db579a0910fac26b01df6d7.svg?invert_in_darkmode&sanitize=true" align=middle width=477.88895714999995pt height=39.452455349999994pt/></p>
<p align="center"><img src="/tex/d09716bc9475610ad344f1c9dbde2549.svg?invert_in_darkmode&sanitize=true" align=middle width=439.92569940000004pt height=62.3703465pt/></p>
<p align="center"><img src="/tex/68e6dff8dc1e273b10728692dcafdd3a.svg?invert_in_darkmode&sanitize=true" align=middle width=502.87851405pt height=38.83491479999999pt/></p>
<p align="center"><img src="/tex/05d2c613a5c5381a851c4fb1b41341e9.svg?invert_in_darkmode&sanitize=true" align=middle width=449.7250032pt height=49.3922088pt/></p>
Where  
m - payment every year  
p - interest rate  
n - number of years  
  
Note - payments for ever (to infinity) example  
<p align="center"><img src="/tex/21fc9ff01047352c464055002254cc01.svg?invert_in_darkmode&sanitize=true" align=middle width=560.3545183499999pt height=39.452455349999994pt/></p>
So for m=USD50K, p=0.06 V=USD883,333

<p align="center"><img src="/tex/1a56b4191d315e9fa9f8c88718090957.svg?invert_in_darkmode&sanitize=true" align=middle width=457.07377814999995pt height=16.438356pt/></p>
<p align="center"><img src="/tex/779a64b3c277ad102cef7a5ff08d943a.svg?invert_in_darkmode&sanitize=true" align=middle width=550.1684859pt height=16.438356pt/></p>
<p align="center"><img src="/tex/7e98dd389c723a47b5921aa7d326cd6e.svg?invert_in_darkmode&sanitize=true" align=middle width=397.5260982pt height=34.3600389pt/></p>

24m
<p align="center"><img src="/tex/93f685518ad66deca91cd73b20ac729b.svg?invert_in_darkmode&sanitize=true" align=middle width=205.2886077pt height=44.89738935pt/></p>


42m
<p align="center"><img src="/tex/76db6f470131f62413e8d47f49ea84de.svg?invert_in_darkmode&sanitize=true" align=middle width=183.42341985pt height=44.89738935pt/></p>
Proof by induction guess is comes out cubic
<p align="center"><img src="/tex/eff3f6f00c6db6383bbdab3d2affceee.svg?invert_in_darkmode&sanitize=true" align=middle width=464.7673437pt height=44.89738935pt/></p>
<p align="center"><img src="/tex/f786e27666b733e6281c7b33d92a6329.svg?invert_in_darkmode&sanitize=true" align=middle width=275.98299629999997pt height=73.78996185pt/></p>
Solve simultaneous equations and and then prove corectness by induction (plugging values in to make sure its correct)

46m-55m50 - Note formula - on test

### 6.042 2010 - R12 -  Sums & Asymptotics 
[Problems for recitation 12](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec12_sol.pdf) ~
[Solutions](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec12_sol.pdf)  
#### 1 The L-tower problem
#### 2 Double Sums

### 6.042 2010 - L13 -  Sums & Asymptotics 
[vid](https://www.youtube.com/watch?v=X9eErxRjQEI) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/MIT6_042JF10_chap09.pdf) ~ 
[Problems](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec13.pdf) ~ 
[Solutions](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec13_sol.pdf) ~ 
Reading:

#### Vid contents
**0m-12m** - Greedy Balancing (L-tower problem?) class demo  
**12m-18m** Greedy algorithm analysis - problem statement   
**14m** - Defining variables  
**18m-21m** - recursive computation for centre of gravity  
**m-m** -   
**m-m** -   
**m-m** -   
**m-m** -   
**m-m** -   
**m-m** -   



#### Notes
**Greedy algorithm analysis**
Basics: push the top block out as far as possible, then the one underneath, then the next etc  

![Stacked block diagram](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/images/_maths_6.042J_L13_17m.png)  

Furthest out block is block out over the edge is block 1, the far edge of which is at r1.  
Each block is length 1.  
Subset of blocks k.  
Block resting on table is nth block, the table itself n+1.  

**Stability constraint:** The centre of mass of block k, Ck, must lie on the block below (k+1) - the table being n+1
For the greedy algorithm centre of mass Ck is\\
right at the edge of the block below,
<p align="center"><img src="/tex/ae8fa4f34f706e0a023a313c8f0cdd39.svg?invert_in_darkmode&sanitize=true" align=middle width=73.08069449999999pt height=15.068469899999998pt/></p>
Centre of mass kth block is at
<p align="center"><img src="/tex/ac52897e5def3d8214ad59c03455f157.svg?invert_in_darkmode&sanitize=true" align=middle width=424.19348564999996pt height=32.990165999999995pt/></p>
Centre of mass of the top k blocks is
<p align="center"><img src="/tex/f240f2408b004b3efff542027fb2d01e.svg?invert_in_darkmode&sanitize=true" align=middle width=222.3168024pt height=85.17131205pt/></p>
in english
<p align="center"><img src="/tex/6b56a3ed2cfa275fad204b6957048bfa.svg?invert_in_darkmode&sanitize=true" align=middle width=737.5649885999999pt height=56.91713114999999pt/></p>
Substituting
<p align="center"><img src="/tex/dd89dfe663a6eda5a9992aa42a8053ef.svg?invert_in_darkmode&sanitize=true" align=middle width=211.0299774pt height=280.3401348pt/></p>




### Problems
6.042 L13 Asymptotic Notation Problems


6.042 L13 Asymptotic Notation Above Problems w/ Solutions


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
Understand - Power, Factorial, Fibonacci Recurrence Solutions



#### Notes

#### References
[Discrete Mathematics] Homogeneous Recurrence Relations 25m 


Solving Divide and Conquer Recurrences 22m - Ref to Text book  


Power, Factorial, Fibonacci Recurrence Solutions

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
<p align="center"><img src="/tex/365ef2065a5108e48b0b4612da56d011.svg?invert_in_darkmode&sanitize=true" align=middle width=414.42354854999996pt height=105.20548004999999pt/></p>

[Recurrence Relations](https://www.youtube.com/watch?v=eAaP4XaB8hM) Discrete Mathematics 15m   
Also see p303 MIT Recurrences - C10  

In an example series: 0	2	6	12	20	30  
Where the difference between element is 2n  
<p align="center"><img src="/tex/6d0986d910306d65abc9c4c5b76b6e85.svg?invert_in_darkmode&sanitize=true" align=middle width=401.72942205pt height=46.0273968pt/></p>

Thats to say where the difference between one element in the sequence and the next is constant (k in this equation) and the base case is c the following holds:  
<p align="center"><img src="/tex/4cd90702be576c3a7ed0351c67c18f50.svg?invert_in_darkmode&sanitize=true" align=middle width=401.2965165pt height=44.89738935pt/></p>

Note: (summation proof @ 14m)  
<p align="center"><img src="/tex/8182cc03706f858356e39b08f4cc0a9d.svg?invert_in_darkmode&sanitize=true" align=middle width=409.5568059pt height=44.89738935pt/></p>



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
<p align="center"><img src="/tex/a5a3fa25cf152acc801491db474d6460.svg?invert_in_darkmode&sanitize=true" align=middle width=407.98942304999997pt height=64.10978970000001pt/></p>



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

