from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/sillicon_valley_summary.csv', index_col=0)
print(df)

print(df.loc['Managers'])
onlyManager = df.loc['Managers', :]
#print(onlyManager)
bool1 = onlyManager['gender'] == 'Male'
#print(onlyManager[bool1])
bool2 = onlyManager['race_ethnicity'] != 'All'
#print()

data = onlyManager[bool2 & bool1]
#data.drop('percentage', axis='columns', inplace=True)
data.plot(kind='bar', x='race_ethnicity', y='count')
print(df.loc['Managers', :])
plt.legend(loc='upper right')
plt.show()