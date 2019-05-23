from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/nation.csv', index_col=0)
df[["Korea_Rep", "United_States", "United_Kingdom", "Germany", "China", "Japan"]].plot()
plt.legend(loc='upper left')
plt.show()

print(df)