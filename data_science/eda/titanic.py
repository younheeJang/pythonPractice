from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/titanic.csv', index_col=0)

#컬럼 뽑기
print(df.columns)


#이번:true
print(df.corr()['Age'].sort_values(ascending=False))
#sns.jointplot(data=df, x='Age', y='Fare')
#sns.clustermap(age_corr)

#삼번:false
print(df['Survived'].value_counts())
surv = df['Survived'].value_counts()
#surv.plot(kind='bar')

#사번:true
Pclass = df['Pclass'].value_counts()
#Pclass.plot(kind='bar')

#오번:
#뭉탱이 뽑자
interests = df.loc[:, 'Survived':'Embarked']
#sns.kdeplot(df['Pclass'], df['Survived'])
#일번:false
#df.plot(kind='hist', y='Age', bins=15)

#육번:false
#sns.catplot(data=df, x='Survived', y='Age', kind='strip')


#칠
sns.stripplot(data=df, x="Survived", y="Age", hue="Sex")
plt.show()
