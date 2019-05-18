import pandas as pd

mega_millions = pd.read_csv("../data/mega_millions.csv", index_col=0)
#mega_millions = pd.read_csv("../data/mega_millions.csv", index_col="Draw Date") 직접 컬럼의 이름 명시도 같음

print(mega_millions)
print(type(mega_millions))