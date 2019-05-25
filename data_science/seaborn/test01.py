from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('../data/body.csv', index_col=0)
print(df)

sns.kdeplot(df['Height'], bw=0.01)
plt.show()
#인덱스가 키이므로, 키순으로 정렬
#df['Height'].value_counts().sort_index().plot()



