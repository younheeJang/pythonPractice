from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/movie_metadata.csv')

print(df)
print(df.columns)

print(df.corr())

#df.plot.scatter(x='budget', y='imdb_score')
#plt.show()
