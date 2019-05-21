import numpy as np
import pandas as pd

df = pd.read_csv('../data/puzzle.csv')

# 코드를 작성하세요.

# 정답 출력
df["A"] = df["A"] * 2
df.iloc[2, 5] = 99
bool1 = df.loc[:, "B":"E"] >= 80
df.loc[:, "B":"E"] = (bool1).astype(int)
#df[df.loc[:, 'B':'E'] < 80] = 0
#df.replace(False, "0", inplace = True)
#df.replace(True, "1", inplace = True)
#df = df.apply(lambda x: x*2)

print(df)