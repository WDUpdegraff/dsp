[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Overall, the plots seem consistent with the values being random.

Probability Mass Function:

![Image of Histogram](https://raw.githubusercontent.com/WDUpdegraff/dsp/master/histogram%20pmf.png)
![Image of PMF](https://raw.githubusercontent.com/WDUpdegraff/dsp/master/pmf.png)

Cumulative Mass Function:

![Image of CMF](https://raw.githubusercontent.com/WDUpdegraff/dsp/master/cumulative.png)

```
import numpy as np
import matplotlib.pyplot as plt
import random
import thinkstats2
import thinkplot

N = 1000#total rands
bins = 30
A_list = [None]*N
i=0
while i<N:
    A_list[i] = random.random()
    i=i+1

A = np.array(A_list)
weights = np.ones_like(A_list)/len(A_list)
fig1 = plt.figure()
plt.hist(A,bins=bins,weights=weights)
plt.title('Probability Mass Function Histogram')
plt.xlabel('Value of random.random')
plt.ylabel('Fraction of counts in bin')
plt.xlim([0,1])

fig2 = plt.figure()
pmf = thinkstats2.Pmf(A_list)
thinkplot.Pmf(pmf, linewidth=0.03)
plt.title('Probability Mass Function')
plt.xlabel('Value of random.random')
plt.ylabel('Probability Mass (0.001 = 1 count)')

B = np.zeros([N,1])
C = np.zeros([N,1])
i=0
while i<N:
    m = (i+1)/N
    l = i/N
    B[i]=len(A[np.where(A < m)])/N
    C[i]=len(A[np.where((A-l) < m)])/N
    i=i+1
ind = np.arange(N)/N
fig3=plt.figure()
plt.bar(ind,B)
plt.title('Cumulative Probability')
plt.xlabel('Value of random.random')
plt.ylabel('Fraction of counts')
plt.xlim([0,1])
plt.ylim([0,1])
```
