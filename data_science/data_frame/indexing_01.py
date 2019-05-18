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
print(iphone_dataframe.iloc[3:, 1:4])
#첫번쨰 행에 헤더가 없는 경우,
#iphone_dataframe = pd.read_csv("../data/iphone.csv", header=None)

#특정 컬럼(0)으로 로우를 구성할 경우
#iphone_dataframe = pd.read_csv("../data/iphone.csv", index_col=0)



