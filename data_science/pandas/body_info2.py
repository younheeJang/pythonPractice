import pandas as pd

df = pd.read_csv('../data/body_info2.csv', index_col=0)


df['비만도'] = '정상'
df.loc[:11, 'Gender'] = 'male'
df.loc[11:, 'Gender'] = 'female'


print(df)