from matplotlib import pyplot as plt
import pandas as pd


df = pd.read_csv('../data/sports.csv', index_col=0)
print(df)

#세로바
#df.plot(kind='bar')
#가로바
#df.plot(kind='barh')
#stacked 옵션
#df.plot(kind='bar', stacked=True)

#시리즈별
df['Female'].plot(kind='bar')
plt.show()