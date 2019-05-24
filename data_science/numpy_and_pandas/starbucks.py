from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/starbucks.csv', index_col=0)

print(df)
print(df.columns)
df.plot(kind='hist', y='Calories', bins=20)

plt.legend(loc='upper left')
plt.show()
