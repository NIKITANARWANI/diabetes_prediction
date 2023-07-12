#Creation of Model
#import lib
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
#load data
data=pd.read_csv("diabetes_m23.csv")
print(data)
#chck data
data[["Glucose",  "BloodPressure",  "SkinThickness" , "Insulin",  "BMI"]]=data[["Glucose",  "BloodPressure",  "SkinThickness" , "Insulin",  "BMI"]].replace(0,np.NAN)
#check for null data
print(data.isnull().sum())
#handle null data
data.fillna({
    "Glucose":data["Glucose"].mean(),  
    "BloodPressure":data["BloodPressure"].mean(),  
    "SkinThickness":data["SkinThickness"].mean(), 
    "Insulin":data["Insulin"].mean(),  
    "BMI":data["BMI"].mean(),
},inplace=True)
print(data.isnull().sum())
#feature and target
features=data.drop("Outcome",axis="columns")
target=data["Outcome"]
print(features)
print(target)

#feature Scaling
mms=MinMaxScaler()
nfeatures=mms.fit_transform(features)
print(nfeatures)

#find value of N
N=int(len(data)**0.5)
if N%2==0:
    N=N+1
    
#train and test
x_train,x_test,y_train,y_test=train_test_split(nfeatures,target)
#model 
model=KNeighborsClassifier(n_neighbors=N,metric="euclidean")
model.fit(x_train,y_train)
#save the model
f=open("de.model","wb")
pickle.dump(model,f)
f.close()