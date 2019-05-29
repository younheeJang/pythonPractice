import pandas as pd

df = pd.read_csv('../data/dust.csv', index_col=0)

print(df)
print(df.index.value_counts())
print(df.loc['07월 31일'])
#중복되는 로우 지우기.
df.drop_duplicates(inplace=True)
print(df.index.value_counts())

print(df.columns.value_counts())

#로우랑 컬럼 바꿔주기
print(df.T)

#그런 상태에서 지우자
df.T.drop_duplicates()

print(df.T.drop_duplicates().T)

df = df.T.drop_duplicates().T
print(df)