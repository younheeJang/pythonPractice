import pandas as pd

iphone_dataframe = pd.read_csv("../data/iphone.csv")
iphone_dataframe = pd.read_csv("../data/iphone.csv", index_col=0)
print(iphone_dataframe)
print()

bool1 = iphone_dataframe['디스플레이'] > 5
print(bool1)
print()

res = iphone_dataframe.loc[bool1]
print(res)
print()

bool2 = iphone_dataframe['Face ID'] == 'Yes'
print(bool2)
print()

res2 = iphone_dataframe.loc[bool2]
print(res2)

res3 = iphone_dataframe.loc[bool1 & bool2]
print(res3)

res4 = iphone_dataframe.loc[bool1 | bool2]
print(res4)