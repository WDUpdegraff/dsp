[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

The exact figure depends on how people are being measured. The Blue Man Group may be measuring people's heights exactly, so that people between 5'10.0" and 6'1.0" inches are elligible. However, when people talk about heights, it's usually rounding to the nearest inch; people between 5'9.5" and 5'10.5" will call themselves 5'10". If they take this standard, it would either expand the elligible height range to 5'9.5" - 6'1.5" (if inclusive) or contract it to 5'10.5" - 6'0.5" (if non-inclusive).

I computed all three:

If Blue Man Group applicants are measured with high precision (i.e. elligible height range is from 70.0-73.0 inches):

34.3% of men are elligible for the Blue Man Group

16.8% of men are too tall for the Blue Man Group

49.0% of men are too short for the Blue Man Group

If Blue Man Group applicants are measured to the nearest inch, and that the range is inclusive (i.e. elligible height range is from 69.5-73.5 inches):

44.6% of men are elligible for the Blue Man Group

13.0% of men are too tall for the Blue Man Group

42.4% of men are too short for the Blue Man Group

If Blue Man Group applicants are measured to the nearest inch, and that the range is *not* inclusive (i.e. elligible height range is from 70.5-72.5 inches):

23.3% of men are elligible for the Blue Man Group

21.2% of men are too tall for the Blue Man Group

55.5% of men are too short for the Blue Man Group

```

import scipy.stats as stats

def tocm(feet,inches):
    return 2.54*12*feet+2.54*inches
    
def writemess(minval,maxval,meanval,sigval,nround):
    z_max = (maxval-meanval)/sigval
    z_min = (minval-meanval)/sigval
    Between = stats.norm.cdf(z_max)-stats.norm.cdf(z_min)
    Above = 1-stats.norm.cdf(z_max)
    Below = stats.norm.cdf(z_min)
    return str(round(100*Between,nround))+'% of men are elligible for the Blue Man Group\n'+str(round(100*Above,nround))+'% of men are too tall for the Blue Man Group\n'+str(round(100*Below,nround))+'% of men are too short for the Blue Man Group'

mess1b = writemess(tocm(5,10),tocm(6,1),178,7.7,1)
mess1 = '\nIf Blue Man Group applicants are measured with high precision (i.e. elligible height range is from 70.0-73.0 inches):\n\n'+mess1b
mess2b = writemess(tocm(5,9.5),tocm(6,1.5),178,7.7,1)
mess2 = '\n\nIf Blue Man Group applicants are rounded to the nearest inch, and that the range is inclusive (i.e. elligible height range is from 69.5-73.5 inches):\n\n'+mess2b
mess3b = writemess(tocm(5,10.5),tocm(6,0.5),178,7.7,1)
mess3 = '\n\nIf Blue Man Group applicants are rounded to the nearest inch, and that the range is *not* inclusive (i.e. elligible height range is from 70.5-72.5 inches):\n\n'+mess3b

print(mess1+mess2+mess3)

```
