import pandas as pd
import matplotlib.pyplot as plt
path = "IRIS.csv"
#df = pd.read_csv(path)
df = pd.read_csv(path,header=None)
header = ["sepal length","sepal-width","petal length","petal width","species"]
s=["sepal length","sepal-width","petal length","petal width"]
df.columns = header
print (df.head(5))
print (df.tail(5))
print (df.info())				
print (df.dtypes)			
print (df.shape)				
print (df.describe())
print (df.describe(include="all"))
d=df.drop(['species'],axis=1)		
	
plt.scatter(df['sepal length'],df['petal length'])
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
#plt.show()
df.hist()



df.plot.box(grid='on')
plt.show()
