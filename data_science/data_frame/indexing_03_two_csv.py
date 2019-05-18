import pandas as pd

samsung = pd.read_csv('../data/samsung.csv')
hyundai = pd.read_csv('../data/hyundai.csv')



print(samsung)
print(hyundai)

#day = samsung['요일']
day = ['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun']
sam = samsung['문화생활비']
hy = hyundai['문화생활비']

dict1 = {
    'day': day,
    'samsung': sam,
    'hyundai': hy
}


di = pd.DataFrame(dict1)
print(di)