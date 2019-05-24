from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/broadcast1.csv', index_col=0)
print(df)

print(df.loc[2017])
df.loc[2017].plot(kind='pie')

#df.plot()
plt.legend(loc='upper left')
plt.show()

