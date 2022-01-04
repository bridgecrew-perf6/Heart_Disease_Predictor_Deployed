import numpy as np
from numpy.core.defchararray import index
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import os


def disease_predictor(temp):
    df=pd.read_csv('heart.csv')
    X=df.drop(columns = 'HeartDisease')
    X.loc[len(X)]=temp
    X=pd.get_dummies(X)
    y = df['HeartDisease']
    clf= LinearRegression()
    X1=X.iloc[:918,:]
    
    clf.fit(X1,y)
    
    y_pred=clf.predict(X1)
    print(r2_score(y,y_pred))
    X_ip=X.loc[len(X)-1]
    X_ip=pd.DataFrame(X_ip).T                            
    r=clf.predict(X_ip)
    if r[0]==0:
        result="You don't Have Heart Disease"
    else:
        result="You have Heart Disease"
    return result

# a=[39,'M','NAP',120,339,0,'Normal',170,'N',0,'Up']
# print(disease_predictor(a))
