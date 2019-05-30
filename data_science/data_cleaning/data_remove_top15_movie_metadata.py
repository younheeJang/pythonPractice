from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/movie_metadata.csv')

print(df)
print(df.columns)
condition = df['budget'].sort_values(ascending=False)
#print(condition[:15]) == print(condition.head(15))
df.drop(condition[:15].index, inplace=True)
df.plot(kind='scatter', x='budget', y='imdb_score')
plt.show()
