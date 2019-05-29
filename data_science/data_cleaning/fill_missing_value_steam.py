import pandas as pd

df = pd.read_csv('../data/steam.csv')

print(df)
print(df.isnull().sum())
print(df.dropna())