[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Cohen's D metric suggests firstborn babies are about 0.09 pounds (1.21%) lighter than others and that first pregnancies are about 0.03 weeks (0.073%) longer than others.

This suggests that there is a real -- though not particularly large -- difference in the weight of first babies which might have some small impact on infant health. The difference in the length of first pregnancy is effectively trivial (about 4 hours).

```
import nsfg
import math

#I used mostly my own code here
def myvar(A):#A is col of data frame with nan, etc removed
    return ((A-A.mean())**2).sum()/(len(A)-1)

#pooled standard deviation
def psd(A,B):
    nA, nB = len(A), len(B)
    vA, vB = myvar(A), myvar(B)
    return math.sqrt(((nA-1)*vA+(nB-1)*vB)/(nA+nB-2))
 
def cohens_d(A,B):
    return (A.mean()-B.mean())/psd(A,B)
    
#good for simple rounding of low numbers
#m is the maximum number of sig figs you want to show
#it will always show to at least integer precision
def roundpretty(A,m):
    n = -1*int(math.log10(A))+m
    if n>0:
        return round(A,n)
    else:
        return round(A)    

#A = weight/len/etc diff (a-b), B = mean of b terms
#unit = unit for the quantity in question e.g. 'pounds'
#moreterm and lessterm are words for comparing quantities
#e.g. heavier, lighter, shorter, longer
#m is a rounding val
def writemess(A,B,unit,moreterm,lessterm,m):
    if A>0:
        status = moreterm
    else:
        status = lessterm
    s1 = str(round(abs(A),2))
    s2 = str(roundpretty((100*abs(A)/B),m))
    return s1 + ' ' + unit + ' (' + s2 + '%) '+status

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
#cleans up negative or nan
firstweights = firsts.totalwgt_lb[firsts.totalwgt_lb > 0]
otherweights = others.totalwgt_lb[others.totalwgt_lb > 0]
firstlengths = firsts.prglngth[firsts.totalwgt_lb > 0]
otherlengths = others.prglngth[others.totalwgt_lb > 0]

wt_F_O = cohens_d(firstweights, otherweights)
ln_F_O = cohens_d(firstlengths,otherlengths)
wtmn = otherweights.mean()
lnmn = otherlengths.mean()
messwt = writemess(wt_F_O,wtmn,'pounds','heavier','lighter',2)
messln = writemess(ln_F_O,lnmn,'weeks','longer','shorter',2)

A = "\nCohen's D metric suggests firstborn babies are about "
B = " than others and that first pregnancies are about "
C = " than others.\n"

print(A+messwt+B+messln+C)
```
