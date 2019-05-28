from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

price_df = pd.read_csv('../data/vegetable_price.csv')
quantity_df = pd.read_csv('../data/vegetable_quantity.csv')

print(price_df)
print(quantity_df)


#inner join: 기준이 되는 컬럼의 교집합
print(pd.merge(price_df, quantity_df, on="Product"))


#left outer join: 왼쪽 데이터 프레임기준으로 합치고, 오른쪽에 없는 컬럼도 만들어버리는데 이 떄 값이 NaN
print(pd.merge(price_df, quantity_df, on="Product", how="left"))

#right outer join: 위와 반대
print(pd.merge(price_df, quantity_df, on="Product", how="right"))

#full outer join: 무엇이 비어있든지 다 넌
print(pd.merge(price_df, quantity_df, on="Product", how="outer"))
