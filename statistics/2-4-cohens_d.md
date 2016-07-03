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
#m is how many sig figs you're gonna show, unless that truncates an integer and leaves zeros
def roundpretty(A,m):
    n = -1*int(math.log10(A))+m
    if n>0:
        return round(A,n)
    else:
        return round(A)    

#A = weight/len/etc diff (a-b), B = mean of b terms
#unit = unit for the quantity in question e.g. 'pounds'
#moreterm and lessterm are terms for comparing quantities of the relevant unit (e.g. 'heavier')
#m is a rounding val
def writemess(A,B,unit,moreterm,lessterm,m):
    if A>0:
        status = moreterm
    else:
        status = lessterm
    return str(round(abs(A),2))+' '+unit+' ('+str(roundpretty((100*abs(A)/B),m))+'%) '+status

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
firstweights = firsts.totalwgt_lb[firsts.totalwgt_lb > 0]#cleans up negative or nan
otherweights = others.totalwgt_lb[others.totalwgt_lb > 0]
firstlengths = firsts.prglngth[firsts.totalwgt_lb > 0]
otherlengths = others.prglngth[others.totalwgt_lb > 0]

wt_F_O = cohens_d(firstweights, otherweights)
ln_F_O = cohens_d(firstlengths,otherlengths)
messwt = writemess(wt_F_O,otherweights.mean(),'pounds','heavier','lighter',2)
messln = writemess(ln_F_O,otherlengths.mean(),'weeks','longer','shorter',2)

print("\nCohen's D metric suggests firstborn babies are about "+messwt+" than others and that first pregnancies are about "+messln+' than others.\n')
```
