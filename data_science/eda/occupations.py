from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/occupations.csv', index_col=0)
bool1 = df['gender'] == 'F'
bool2 = df['gender'] == 'M'
print(df[bool1])

data = df[bool1]
data1 = df[bool2]
print(data['occupation'].value_counts())
print(data1['occupation'].value_counts())
#plt.show()



