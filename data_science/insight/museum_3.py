from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/museun_3.csv')

#컬럼 뽑기
print(df)

#df = df.rename(columns={'지역번호': '지역명'})

print(df)

#컬럼명 변경 후 데이터 프레임 변경에 활용할 딕셔너리를 만든다.

local_seperating = {
    '2': '서울시',
    '32' : '경기도',
    '33' : '강원도',
    '41' : '충청도',
    '42' : '충청도',
    '31' : '경기도',
    '43' : '충청도',
    '44' : '충청도',
    '51' : '부산시;',
    '52' : '경상도',
    '53' : '경상도',
    '54' : '경상도',
    '55' : '경상도',
    '61' : '전라도',
    '62' : '전라도',
    '63' : '전라도',
    '64' : '제주도',
    '1577': '기타',
    '070': '기타'
}
df = df.astype({'지역번호':str})
df['지역번호'] = df['지역번호'].map(local_seperating)
print(df['지역번호'].dtype)
df = df.rename(columns={'지역번호': '지역명'})
print(df)
