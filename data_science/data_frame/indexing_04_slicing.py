import pandas as pd

iphone_dataframe = pd.read_csv("../data/iphone.csv")
iphone_dataframe = pd.read_csv("../data/iphone.csv", index_col=0)
print(iphone_dataframe)
print(iphone_dataframe.loc['iPhone 7':'iPhone X'])
print(iphone_dataframe.loc[:, '메모리':'출시 버전'])

print(iphone_dataframe.loc['iPhone 7':'iPhone X', '메모리':'출시 버전'])