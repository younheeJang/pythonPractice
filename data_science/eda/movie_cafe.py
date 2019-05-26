from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/young_survey.csv', index_col=0)

print(df)

#뭉탱이 뽑자
interests = df.loc[:, 'Horror':'Action']
print(interests.head())
#관심사들의 상관관계
print(interests.corr())
corr = interests.corr()

#뭉탱이로 분석하기 위해서
sns.clustermap(corr)
plt.show()
