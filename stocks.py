import sys
import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


offset=0

while(offset<1):
    offset=int(input("How many days would you like to project? "))

simple=input("Would you like simple output or advanced? Y/n for Simple.")
offset=-offset
df=pd.read_csv(sys.argv[1],sep=',')
df=df[[' Close/Last']]
df['Pred']=df[[' Close/Last']].shift(offset)
nparr=np.array(df.drop(['Pred'],1))
nparr=nparr[:offset]
x=[]
for j in nparr:
    for i in j:
        x.append([float(i.replace('$',''))])
x=np.array(x[::-1])
arr2=np.array(df['Pred'])
arr2=arr2[:offset]
y=[]
for k in arr2:
    y.append(float(k.replace('$','')))
y=np.array(y[::-1])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
svr=SVR(kernel='rbf',C=1e3,gamma=0.1)
svr.fit(x_train,y_train)
svmscore=svr.score(x_test,y_test)

reg=LinearRegression()
reg.fit(x_train,y_train)
lrscore=reg.score(x_test,y_test)
prediction=np.array(df.drop(['Pred'],1))[:-offset]
p=[]
for j in prediction:
    for i in j:
        p.append([float(i.replace('$',''))])
p=np.array(p[::-1])
if(svmscore>0.7):
    print("Support Vector Model:\n$" + str(svr.predict(p)[-1]) +"with score" + str(svmscore))
else:
    print("SVM model not accurate.")
if(lrscore>0.7):
    print("Linear Regression Model:\n$" + str(reg.predict(p)[-1]) + " with score "+str(lrscore))

else:
    print("Linear Regression not accurate")
