from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/exam.csv', index_col=0)
print(df)
print(df['math score'].describe())

#df.plot(kind='box', y='math score')
#df.plot(kind='box', y=['math score', 'reading score', 'writing score'])
df.plot(kind='scatter', x='math score', y='reading score')
#plt.legend(loc='upper left')
plt.show()