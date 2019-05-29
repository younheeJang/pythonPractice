from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/beer.csv')

print(df)
print(df.columns)

#이상점 차장내기
print(df['abv'].describe())
#지점 받아오기
print(df['abv'].quantile(0.25))

#
q1 = df['abv'].quantile(0.25)
q3 = df['abv'].quantile(0.75)
iqr = q3 - q1

#이상점을 찾기 위한 범위.
condition = (df['abv'] < q1 - 1.5 * iqr) | (df['abv'] > q3 + 1.5 * iqr)
#데이터 프레임에서 이상점을 기준으로 뽑기
print(df[condition])

#컬럼의 값만 바꾸면 될 때.
df.loc[2250, 'abv'] = 0.055

print(df.loc[2250])

#고친 후 이상점 다시 잡기
condition = (df['abv'] < q1 - 1.5 * iqr) | (df['abv'] > q3 + 1.5 * iqr)

#애초에 잘못들어간 애들은 걍 지우기
#이상점들의 인덱스
print(df[condition].index)
df.drop(df[condition].index, inplace=True)

df.plot(kind='box', y='abv')
plt.show()