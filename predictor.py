import sys
import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

df=pd.read_csv(sys.argv[1],sep=',')
df=df[[' Close/Last']]
offset=-30 #measured in days
df['Pred']=df[[' Close/Last']].shift(offset)
nparr=np.array(df.drop(['Pred'],1))
nparr=nparr[:offset]
x=[]
for j in nparr:
    for i in j:
        x.append([float(i.replace('$',''))])
x=np.array(x)
print(x)
arr2=np.array(df['Pred'])
arr2=arr2[:offset]
y=[]
for k in arr2:
    y.append(float(k.replace('$','')))
y=np.array(y)
'''
data=open(sys.argv[1])
stockdat=csv.DictReader(data,delimiter=',')
for line in stockdat:
    high=float(line[' High'].replace('$',''))
    low=float(line[' Low'].replace('$',''))
    op=float(line[' Open'].replace('$',''))
    print(high)
    print(low)
'''
