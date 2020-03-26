import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
headers=['Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome']
df=pd.read_csv("diabetes.csv")

#Replacing missing values by Mean

mean_glucose = df['Glucose'].mean(skipna=True)
df['Glucose'] = df['Glucose'].replace(0,mean_glucose)

mean_bp = df['BloodPressure'].mean(skipna=True)
df['BloodPressure'] = df['BloodPressure'].replace(0,mean_bp)

mean_st = df['SkinThickness'].mean(skipna=True)
df['SkinThickness'] = df['SkinThickness'].replace(0,mean_st)

mean_Insulin = df['Insulin'].mean(skipna=True)
df['Insulin'] = df['Insulin'].replace(0,mean_Insulin)

mean_BMI = df['BMI'].mean(skipna=True)
df['BMI'] = df['BMI'].replace(0,mean_BMI)

mean_DiabetesPedigreeFunction = df['DiabetesPedigreeFunction'].mean(skipna=True)
df['DiabetesPedigreeFunction'] = df['DiabetesPedigreeFunction'].replace(0,mean_DiabetesPedigreeFunction)

mean_Age = df['Age'].mean(skipna=True)
df['Age'] = df['Age'].replace(0,mean_Age)

#print(df[0:10])


'''
#perform scaling (NORMALIZATION)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1), copy=False)
print(scaler.fit(df))
df = scaler.transform(df)

print(df)
'''

#Model Creation

from sklearn.model_selection import train_test_split

#using all input labels
X = np.array(df.drop(['Outcome'],axis=1))
y = np.array(df['Outcome'])
'''

#for only input label BMI and Age
X = np.array(df.drop(['Outcome','Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','DiabetesPedigreeFunction'],axis=1))
y = np.array(df['Outcome'])

'''
#print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=56)

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, y)
y_predict = clf.predict(X_test)

from sklearn.metrics import confusion_matrix
c=confusion_matrix(y_test,y_predict)
print("Confusion Matrix:")
print(c)
'''
from sklearn.metrics import precision_recall_fscore_support
prfs=precision_recall_fscore_support(y_test,y_predict)
print("prediction",prfs[0])
'''
from sklearn.metrics import accuracy_score
print("Accuracy using Naive Bayes is:");
print(accuracy_score(y_test, y_predict))

