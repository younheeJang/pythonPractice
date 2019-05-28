from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/occupations_2.csv')


#컬럼 뽑기
print(df)
#df.sort_values('age', ascending=False).groupby('occupation').head(3)

grouping = df.groupby('occupation')

print(grouping.mean().sort_values(by='age'))
print(type(grouping))
print(grouping['age'])
print(type(grouping.mean().sort_values(by='age')))
