from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/musium.csv')

#컬럼 뽑기
print(df)

print(df['운영기관전화번호'].str.split('-', n=1))
input = df['운영기관전화번호'].str.split('-', n=1, expand=True)
df['지역번호'] = input[0]

print(df)