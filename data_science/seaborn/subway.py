from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('../data/subway.csv', index_col=0)
print(df)

#히스토
#df.plot(kind='hist', y='out', bins=15)

#박스
#df.plot(kind='box', y='out')

#씨본 kde
#sns.kdeplot(df['in'])

#씨본 + 히스토
#sns.distplot(df['out'], bins=15)

#씨본 + 박스
#sns.violinplot(y=df['out'])

#산점도
#df.plot(kind='scatter', x='in', y='out')

#등고선
#sns.kdeplot(df['in'], df['out'])
#sns.kdeplot(df['out'])

sns.lmplot(data=df, x='in', y='out')



plt.show()