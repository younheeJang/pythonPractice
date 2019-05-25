from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('../data/laptops02.csv', index_col=0)
print(df)
print(df['model'].unique())

#카테고리별 분류: 카테고리=x
sns.catplot(data=df, x='os', y='price', kind='swarm', hue='processor_brand')

#sns.kdeplot(df['Height'], bw=0.01)
plt.show()



