import pandas as pd

df = pd.read_csv('../data/world_cities2.csv', index_col=0)
print(df)
print(df['Country'].value_counts())


countries = df['Country'].value_counts()
countries[countries == 4]
print(countries[countries == 4])