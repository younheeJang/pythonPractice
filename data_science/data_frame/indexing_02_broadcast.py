import pandas as pd

broadcast = pd.read_csv('../data/broadcast.csv', index_col=0)
print(broadcast.loc[2016, 'KBS'])
print(broadcast[['JTBC', 'SBS']])
print(broadcast)
print(broadcast.loc[:, 'KBS':'SBS'])

kbs = broadcast.loc[:, 'KBS']
bool1 = kbs > 30
print(kbs.loc[bool1])

sbs = broadcast.loc[:, 'SBS']
cho = broadcast.loc[:, 'TV CHOSUN']
bool2 = sbs < cho
print(bool2)

dict1 = {
    'SBS':sbs,
    'TV CHOSUN':cho
}

sbs_cho = pd.DataFrame(dict1)
print(sbs_cho.loc[bool2])

print(broadcast.loc[bool2, ['SBS', 'TV CHOSUN']])
