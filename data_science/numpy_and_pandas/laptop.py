import pandas as pd

df = pd.read_csv("../data/laptops.csv")
print(df.head(3))
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.sort_values(by="price"))
print(df.sort_values(by="price", ascending=False))
print(df.describe())
print(df.head(3))

#브랜드명 중 중복되는 값 뺀 나머지를 리스트화 하여 리턴
print(df['brand'].unique())

#각 컬럼에 해당하는 값이 총 몇 개씩 있는지.
print(df['brand'].value_counts())

#해당 시리즈에 대한 정보
print(df['brand'].describe())

