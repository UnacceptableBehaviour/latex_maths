Maths - Brush up list
file:/a_syllabus/_COURSES_00_WIP/MATHS_00_MIT_6.042.rtf
REPO: 

Abstract
Maths revision & learning 
[MIT 6.042J](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/syllabus/)  

## Contents  
1. [AIM:](#aim)  
2. [Asymptotic Notation](#asymptotic-notation)  
	1. [6.042 2010 - L12 -  Sums ()](#6042-2010--l12---sums-)  
	2. [Problems](#problems)  
	3. [6.042 2010 - L13 -  Sums & Asymptotics ()](#6042-2010--l13---sums--asymptotics-)  
	4. [6.04J Intro Algorithms L2: Asymptotic Notation | Recurrences | Substitution, Master Method ()](#604j-intro-algorithms-l2-asymptotic-notation--recurrences--substitution-master-method-)  
	5. [References](#references)  
3. [Recurrence resolution for - Algos L3 34m](#recurrence-resolution-for--algos-l3-34m)  
	1. [Problems](#problems)  
	2. [References](#references)  
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

Maths needs to be good enough to support MIT Algorithms course  

Sometimes an equation is unintelligible due to lack of vocabulary / symbol knowledge!!  

A good place to start in this case is wikipedias [List of mathematical symbols by subject](https://en.wikipedia.org/wiki/List_of_mathematical_symbols_by_subject)  
A less intimidating list of [symbols by subject inc greek symbols](https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html#calculus)  
Good to know your [Greek symbols & Latex](https://www.nyu.edu/projects/beber/files/Chang_LaTeX_sheet.pdf)  
Latex [full reference](http://www.icl.utk.edu/~mgates3/docs/latex.pdf)  
Maths on [git](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/context.md)






- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Asymptotic Notation

### 6.042 2010 - L12 -  Sums ()  
List of [Summation identities!](https://en.wikipedia.org/wiki/Summation)    

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

Note where  
<p align="center"><img src="/tex/576b7f10f475d5a1810e619cf4fb077d.svg?invert_in_darkmode&sanitize=true" align=middle width=387.04905525pt height=16.438356pt/></p>
<p align="center"><img src="/tex/805ceda1fbefda94db618e14db46bb51.svg?invert_in_darkmode&sanitize=true" align=middle width=397.53613185pt height=16.438356pt/></p>
<p align="center"><img src="/tex/0a32c348cfbde000fd924ecda1ff67ea.svg?invert_in_darkmode&sanitize=true" align=middle width=376.20334125pt height=16.438356pt/></p>
<p align="center"><img src="/tex/7e98dd389c723a47b5921aa7d326cd6e.svg?invert_in_darkmode&sanitize=true" align=middle width=397.5260982pt height=34.3600389pt/></p>

21m40 geometric series - where <img src="/tex/4c694f868813e387befe5da215680867.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2751585499999pt height=677.077632pt/><img src="/tex/54dc1f929918b73bd30441e0950d0a5a.svg?invert_in_darkmode&sanitize=true" align=middle width=667.3972420499999pt height=166.0273989pt/><img src="/tex/0968d2a2e2571aa105f1264f8cb94286.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2747246pt height=124.74886379999998pt/><img src="/tex/0b0b79ac3904be4b908569ca48782e3d.svg?invert_in_darkmode&sanitize=true" align=middle width=667.3972420499999pt height=47.671232400000015pt/><img src="/tex/c7a9258b4e7b52a39b2349702fa8236c.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2747410999999pt height=87.12328679999997pt/><img src="/tex/79e0d0a5a1649a42042ebf57f5c6c441.svg?invert_in_darkmode&sanitize=true" align=middle width=139.0477407pt height=26.438629799999987pt/><img src="/tex/16fcf0c6ebe245af14d6f32a450110fa.svg?invert_in_darkmode&sanitize=true" align=middle width=222.96870584999996pt height=47.67123239999998pt/><img src="/tex/af2edb9b9dd90cb9956552f2b656063b.svg?invert_in_darkmode&sanitize=true" align=middle width=137.90868629999997pt height=33.20539859999999pt/><img src="/tex/c4c70135c78916e96313c73b192b3ed2.svg?invert_in_darkmode&sanitize=true" align=middle width=2514.7610202pt height=1152.3287655pt/> symbols like so
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

