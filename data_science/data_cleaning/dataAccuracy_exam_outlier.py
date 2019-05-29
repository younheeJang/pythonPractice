from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/exam_outlier.csv')

print(df)
print(df.columns)

#관계적 이상점. 두 컬럼의 관계상 나올 수 없는...... 값.
print(df.corr())
print(df.columns)
#df.corr().plot(kind='bar')
print(type(df.corr()))
#이상점 지우고
print(df[df['writing score'] > 100])
df.drop(51, inplace=True)
#말도 안되는 데이터 이상점 지우고 다시 상관계수를 뽑아보면 더 정확해 짐.
print(df.corr())

#말이 안되는 건 아닌데 평균치랑 너무 떨어진 애 하나 찾고, 지우기
print((df['writing score'] > 90) & (df['reading score'] < 40))
condition = (df['writing score'] > 90) & (df['reading score'] < 40)
print(df[condition])

#찾아서 지우고, 다시 상관관계를 뽑아 봄.
df.drop(373, inplace=True)
print(df.corr())

df.plot.scatter(x='reading score', y='writing score')
plt.show()
