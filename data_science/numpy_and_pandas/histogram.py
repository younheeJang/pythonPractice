from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/body.csv', index_col=0)

print(df)

df.plot(kind='hist', y='Height', bins=15)

plt.legend(loc='upper left')
plt.show()
