import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score

df=pd.read_csv('Dia.csv')
headers=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
df.columns=headers

print(df.head(5))
print(df.tail(5))

# drop preg and outcome as except these columns if other column have 0 value it means it is missing or wrong value and we need  to replace it by mean 
df2=df.drop(['Pregnancies','Outcome'],axis=1)


print(df.head(5))
#find a mean to replace missing values by mean (astype is use to change column type)
avg_insulin=df2['Insulin'].astype("float").mean(axis=0)
avg_glucose=df2['Glucose'].astype("float").mean(axis=0)
avg_bp=df2['BloodPressure'].astype("float").mean(axis=0)
avg_skinthickness=df2['SkinThickness'].astype("float").mean(axis=0)
avg_BMI=df2['BMI'].astype("float").mean(axis=0)
avg_DPF=df2['DiabetesPedigreeFunction'].astype("float").mean(axis=0)
avg_age=df2['Age'].astype("float").mean(axis=0)

#replace zero insulin with mean
#print(avg_2)
df['Insulin'].replace(0,avg_insulin,inplace=True) #make it work to replace zero
df['Glucose'].replace(0,avg_glucose,inplace=True)
df['BloodPressure'].replace(0,avg_bp,inplace=True)
df['SkinThickness'].replace(0,avg_skinthickness,inplace=True)
df['BMI'].replace(0,avg_BMI,inplace=True)
df['DiabetesPedigreeFunction'].replace(0,avg_DPF,inplace=True)
df['Age'].replace(0,avg_age,inplace=True)

#print(df['Insulin']) #to check whether 0 is replaced by mean or not print the column

x=np.array(df.drop(['Outcome'],axis=1))#axis=1 means its a column
y=np.array(df['Outcome'])

#scaling fitting in 0 and 1 range
scaler = MinMaxScaler()
x_scaler=scaler.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(x_scaler,y,test_size=0.2,random_state=0) #0.2 means test=20% train=80% selecting #start from 0 th record 


classifier=GaussianNB()
classifier.fit(x_train,y_train)
y_predict=classifier.predict(x_test)

#validate the prediction
c=confusion_matrix(y_test,y_predict)
cf_df= pd.DataFrame(c,columns=['Predicted No','Predicted Yes'], index=['Actual No', 'Actual yes'])

print(cf_df)

prfs=precision_recall_fscore_support(y_test,y_predict)
acc=accuracy_score(y_test, y_predict)
print(acc)
print("Precision is : %0.2f" % prfs[0])

