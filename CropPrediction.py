import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data=pd.read_csv('crop.csv')
x=data.iloc[:,3:11].values
y=data.iloc[:,11].values

label=LabelEncoder()
x[:,0]=label.fit_transform(x[:,0])
x[:,1]=label.fit_transform(x[:,1])
x[:,2]=label.fit_transform(x[:,2])
x[:,6]=label.fit_transform(x[:,6])

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=33)

main=LinearRegression()
main=main.fit(xtrain,ytrain)

ypred=main.predict(xtest)

r2_score(ytest,ypred)

data=data.drop(['S.NO'], axis=1)
corr=data.corr()

data.head(10)

sns.heatmap(corr,xticklabels=corr.columns,yticklabels=corr.columns,cmap="YlGnBu",annot=True)
yields=data.iloc[:,10].values
seeds=data.iloc[:,2].values
soil=data.iloc[:,4].values
fert=data.iloc[:,8].values
season=data.iloc[:,3].values
humid=data.iloc[:,5].values

# Type of seeds effecting the yield
plt.bar(seeds,yields)
plt.xlabel('seeds', fontsize=10)
plt.ylabel('yield', fontsize=10)
plt.title('SEEDS EFFECTING THE YIELD')
plt.show()

# Type of soil effecting the yield
plt.bar(fert,yields,color='g')
plt.xlabel('fertilizers', fontsize=10)
plt.ylabel('yield', fontsize=10)
plt.title('FERTILIZERS EFFECTING THE YIELD')
plt.show()

# Type of fertilizer effecting the yield
plt.bar(season,yields,color='y')
plt.xlabel('season', fontsize=10)
plt.ylabel('yield', fontsize=10)
plt.title('SEASON EFFECTING THE YIELD')
plt.show()

# Type of season effecting the yield
plt.bar(humid,yields)
plt.xlabel('humidity', fontsize=10)
plt.ylabel('yield', fontsize=10)
plt.title('HUMIDITY EFFECTING THE YIELD')
plt.show()