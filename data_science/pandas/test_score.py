import pandas as pd

ts = pd.read_csv('../data/test_score.csv')


bool1 = ts['LC'] >= 250
bool2 = ts['RC'] >= 250
bool3 = ts['LC'] + ts['RC'] > 600
ts.loc[bool1]

print(ts.loc[bool1 & bool2 & bool3])
print(bool1 & bool2 & bool3)
ts['합격 여부'] = bool1 & bool2 & bool3
print(ts)