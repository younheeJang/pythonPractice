from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/albums.csv', index_col=0)

#문자열 필터링

#컬럼 뽑기
print(df)
print(df['Genre'].unique())
#블루스만 말고 블루스가 들어있기라도 한 컬럼 다
print(df['Genre'].str.contains('Blues'))
print(df[df['Genre'].str.contains('Blues')])
#블루스가 맨 앞인 컬럼 다
print(df[df['Genre'].str.startswith('Blues')])

df['Contains Blues'] = df['Genre'].str.contains('Blues')


print(df)