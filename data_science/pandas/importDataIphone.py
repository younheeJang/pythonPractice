import pandas as pd

iphone_dataframe = pd.read_csv("../data/iphone.csv")
iphone_dataframe
print(iphone_dataframe)
print(type(iphone_dataframe))

#첫번쨰 행에 헤더가 없는 경우,
#iphone_dataframe = pd.read_csv("../data/iphone.csv", header=None)

#특정 컬럼(0)으로 로우를 구성할 경우
#iphone_dataframe = pd.read_csv("../data/iphone.csv", index_col=0)



