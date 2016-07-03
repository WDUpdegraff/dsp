[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The actual mean number of children is 1.024. The biased mean is 2.404. 

![Image of plot](https://raw.githubusercontent.com/WDUpdegraff/dsp/master/actualbiased.png)

```
import pandas as pd
import numpy as np
import survival
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

resp = survival.ReadFemResp()
nums = resp.numkdhh
maxk=pd.DataFrame.max(nums)
mink=pd.DataFrame.min(nums)
k=np.zeros([(maxk-mink+1),1])#family size (k=kids)
A=np.zeros([(maxk-mink+1),1])#Actual
B=np.zeros([(maxk-mink+1),1])#Biased

i=0
while i<(maxk-mink+1):
    n = mink+i
    k[i]=n#family size
    countA = (nums==(mink+i)).sum()#count of families with n kids
    A[i]= countA
    B[i]=countA*n#count of kids in families with n kids
    i=i+1

width = 0.4
plt.bar(k,A,width,color = 'b')
plt.hold(True)
plt.bar(k+width,B,width,color = 'r')

red_patch = mpatches.Patch(color='b', label='Actual')

blue_patch = mpatches.Patch(color='r', label='Biased')
plt.legend(handles=[red_patch, blue_patch])

Amean = float(np.dot(k.transpose(),A)/np.sum(A))#Actual mean
Bmean = float(np.dot(k.transpose(),B)/np.sum(B))#Biased mean
```
