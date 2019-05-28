from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/occupations_2.csv')


#컬럼 뽑기
print(df)
print(df.columns)
print(df['gender'])

df.drop(columns='age', inplace=True)
print(df)

#불리언으로는 mean()함수의 결과를 도출할 수 없으니, 불리언으로 컬럼을 바꾼다.
boolMan = df['gender'] == 'F'
print(boolMan)
df['gender'] = boolMan

#그리고, 불리언으로 바뀐 젠더 컬럼을 다시, 인트로 바꾼다.
print(df['gender'].astype(int))
df['gender'] = df['gender'].astype(int)
print(df)
grouping = df.groupby('occupation')

#직업별로 그루핑한 데이터 프레임 그룹을, 젠더라는 컬럼을 중심으로 솔팅한다.
print(grouping.mean().sort_values(by='gender', ascending=False))
