import pandas as pd

museum = pd.read_csv("../data/musium_3.csv", dtype={'지역번호': str})
number = pd.read_csv("../data/region_number.csv", dtype={'지역번호': str})

print(museum)
print(number)

print(pd.merge(museum, number, on="지역번호", how='left'))