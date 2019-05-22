import pandas as pd

df = pd.read_csv('../data/enrollment_3.csv')

print(df)

#rename column: room assignment to room number:
df.rename(columns={'room assignment':'room number'}, inplace=True)
print(df[df['status'] == 'allowed'].sort_values(by='course name'))
without_not = df['status'] == 'allowed'
print(df['room number'].value_counts())
print(df['course name'].unique())