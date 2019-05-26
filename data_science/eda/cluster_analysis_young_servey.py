from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/young_survey.csv', index_col=0)

print(df)

#뭉탱이 뽑자
interests = df.loc[:, 'History':'Pets']
print(interests.head())
#관심사들의 상관관계
print(interests.corr())
corr = interests.corr()
#역사 컬럼에 대한 상관관계:큰 순서대로 정렬
print(corr['History'].sort_values(ascending=False))

#뭉탱이로 분석하기 위해서
sns.clustermap(corr)
plt.show()
