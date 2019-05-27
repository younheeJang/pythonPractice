from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/musium.csv')

#컬럼 뽑기
print(df)
print(df['시설명'].str.contains('대학'))

bool1 = df['시설명'].str.contains('대학')

print(bool1)
df['분류'] = bool1

print(df)

for i, r in df.iterrows():
    if r['분류'] == True:
        print(r['시설명'])
        df.at[i, '분류'] = '대학'
    else:
        print(r['분류'])
        df.at[i, '분류'] = '일반'


print(df)