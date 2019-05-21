import pandas as pd

df = pd.read_csv('../data/world_cities.csv', index_col=0)

print(df)
print(df['Population'])
print(df['Land area (in sqKm)'])
#print((df['Population']/df['Land area (in sqKm)'] > 1000).astype(int))
df['인구밀도'] = df['Population']/df['Land area (in sqKm)']
#flat = (df['Population']/df['Land area (in sqKm)'] > 1000).astype(int)
#print(flat.value_counts())
print(df)
print(df['인구밀도'].describe())
print(df[df['인구밀도'] > 10000].describe())
print(df[df['인구밀도'] > 10000].sort_values(by='인구밀도').tail(1))