from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/parks.csv')

#컬럼 뽑기
print(df)

#문자열분리:띄어쓰기 기반으로 컬럼안의 문자열을 나눠 리스트화
print(df['소재지도로명주소'].str.split())

#문자열분리:첫번째 띄어쓰기만 따로 떼어내 리스트화
print(df['소재지도로명주소'].str.split(n=1))

#문자열분리:이후 해당 값을 새롭게 리스트화 해서 데이터프레임으로 만들어 리턴
print(df['소재지도로명주소'].str.split(n=1, expand=True))

#활용을 위해 새롭게 리턴된 데이터프레임을 변수에 저장
address = df['소재지도로명주소'].str.split(n=1, expand=True)

#원 데이터 프레임에 새로운 컬럼을 만들어 값 집어넣ㄱ;
df['관할구역'] = address[0]

print(df)