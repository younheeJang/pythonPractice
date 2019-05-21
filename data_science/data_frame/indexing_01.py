import pandas as pd

iphone_dataframe = pd.read_csv("../data/iphone.csv")
iphone_dataframe = pd.read_csv("../data/iphone.csv", index_col=0)
print(iphone_dataframe)
print(type(iphone_dataframe))
print(iphone_dataframe.loc['iPhone 8', '메모리'])
print(iphone_dataframe.loc['iPhone 8', :])
print(type(iphone_dataframe.loc['iPhone 8', :]))
print(iphone_dataframe.loc[:, '출시일'])
print(iphone_dataframe['출시일'])
print(type(iphone_dataframe.loc[:, '출시일']))
print(iphone_dataframe.iloc[2, 4])
print(iphone_dataframe.iloc[[1, 3], [1, 4]])

#추가 삭제
iphone_dataframe.loc['iPhone XR'] = ['2019-10-20', 5.1, '6GB', 'iOS 12.5', 'Yes']
iphone_dataframe['제조사'] = 'apple'
print(iphone_dataframe)
#로우 삭제시 : axis='index', inplace=False(기존 데이터 프레임이 바뀌지 않음
iphone_dataframe.drop('iPhone XR', axis='index', inplace=False)
print(iphone_dataframe)
iphone_dataframe.drop('iPhone XR', axis='index', inplace=True)
print(iphone_dataframe)
#여러 로우를 한번에 지우기
iphone_dataframe.drop(['iPhone 7', 'iPhone 8'], axis="index", inplace=True)
print(iphone_dataframe)
#컬럼 삭제시
iphone_dataframe.drop('제조사', axis='columns', inplace=True)
print(iphone_dataframe)
#첫번쨰 행에 헤더가 없는 경우,
#iphone_dataframe = pd.read_csv("../data/iphone.csv", header=None)

#특정 컬럼(0)으로 로우를 구성할 경우
#iphone_dataframe = pd.read_csv("../data/iphone.csv", index_col=0)



