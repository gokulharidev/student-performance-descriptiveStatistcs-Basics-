import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

stu=pd.read_csv('StudentsPerformance.csv')
math=stu['math score']
read=stu['reading score']
write=stu['writing score']

#method of central tendancy

mm=np.mean(math)
mr=np.mean(read)
mw=np.mean(write)

print("mean :\n math :",mm,",read:",mr,"write:",mw)

math=np.sort(math)
read=np.sort(read)
write=np.sort(write)

mem=np.median(math) 
mer=np.median(read) 
mew=np.median(write) 

print("median :\n math :",mem,",read:",mer,"write:",mew)
from collections import Counter
mathc=Counter(math)
readc=Counter(read)
writec=Counter(write)
modem=mathc.most_common(1)[0][0]
moder=readc.most_common(1)[0][0]
modew=writec.most_common(1)[0][0]

print("mode :\n math :",modem,",read:",moder,"write:",modew)
#method of variability

maxm=max(math)
minm=min(math)
rangem=maxm-minm


maxr=max(read)
minr=min(read)
ranger=maxr-minr


maxw=max(write)
minw=min(write)
rangew=maxw-minw

print("range :\n math :",rangem,",read:",ranger,"write:",rangew)
varm=np.var(math)
varr=np.var(read)
varw=np.var(write)

print("variancde :\n math :",varm,",read:",varr,"write:",varw)
stdm=np.std(math)
stdr=np.std(read)
stdw=np.std(write)

print("standard deviation :\n math :",stdm,",read:",stdr,"write:",stdw)


#mehtod of shape

from scipy.stats import skew
skewm = skew(math)
skewr = skew(read)
skeww = skew(write)

print("Skewness :\n math:", skewm, ", read:", skewr, ", write:", skeww)


from scipy.stats import kurtosis

kurtm = kurtosis(math)
kurtr = kurtosis(read)
kurtw = kurtosis(write)

print("Kurtosis :\n math:", kurtm, ", read:", kurtr, ", write:", kurtw)

p25m = np.percentile(math, 25)
p75m = np.percentile(math, 75)

p25r = np.percentile(read, 25)
p75r = np.percentile(read, 75)

p25w = np.percentile(write, 25)
p75w = np.percentile(write, 75)

print("Percentiles (25th & 75th):\n math: (", p25m, ",", p75m, "), read: (", p25r, ",", p75r, "), write: (", p25w, ",", p75w, ")")

correlation_matrix = stu[['math score', 'reading score', 'writing score']].corr()
print("Correlation Matrix:\n", correlation_matrix)

# Heatmap for better visualization
import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.show()

