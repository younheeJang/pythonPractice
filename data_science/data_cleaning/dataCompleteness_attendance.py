import pandas as pd

df = pd.read_csv('../data/attendance.csv')

print(df)

#isNull : True : NaN
print(df.isnull())

#널의 개수: 컬럼별 결측값의 개수
print(df.isnull().sum())

#결측값 없애기 -> 데이터의 완결성 추구
#결측값 있는 로우 아예 없애기. 새로운 데이터 프레임화.
print(df.dropna())
#print(df.dropna(inplace=True))

#결측값이 있는 컬럼을 모두 지운다.
print(df.dropna(axis='columns'))

#로우나 컬럼 자체를 없애버리기 보다 결측값을 채워줄 수도 있음:평균값
print(df.fillna(df.mean()))

#로우나 컬럼 자체를 없애버리기 보다 결측값을 채워줄 수도 있음:중간값
print(df.fillna(df.median()))

#바뀐 것을 기존 데이터 프레임에 적용시키고 싶다면, inplace



