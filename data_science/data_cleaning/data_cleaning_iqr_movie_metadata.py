from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/movie_metadata.csv')

print(df)
print(df.columns)

print(df.corr())
q1 = df['budget'].quantile(0.25)
q3 = df['budget'].quantile(0.75)
iqr = q3 - q1
print(iqr)
print(df.describe())
condition = (df['budget'] > q3 + 5 * iqr)

#애초에 잘못들어간 애들은 걍 지우기
#이상점들의 인덱스
print(df[condition].index)
df.drop(df[condition].index, inplace=True)
print(df)
df.plot.scatter(x='budget', y='imdb_score')
plt.show()
