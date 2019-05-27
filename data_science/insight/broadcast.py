from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/broadcast.csv', index_col=0)

#컬럼 뽑기
print(df)
#df.plot()
#total = df['KBS'] + df['MBC'] + df['SBS'] + df['TV CHOSUN'] + df['JTBC'] + df['Channel A'] + df['MBN']
total = df.sum(axis="columns")
print(total)
df['Total'] = total

df['Group 1'] = df.loc[:, 'KBS':'SBS'].sum(axis="columns")
df['Group 2'] = df.loc[:, 'TV CHOSUN':'MBN'].sum(axis="columns")
print(df)
df.plot(y=["Group 1", "Group 2"])
plt.show()
