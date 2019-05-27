from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/laptops_nation.csv')


#컬럼 뽑기
print(df.columns)

brand_nation = {
    'Dell' : 'U.S',
    'Apple' : 'U.S',
    'Acer' : 'Taiwan',
    'HP' : 'U.S',
    'Lenovo' : 'China',
    'Alienware' : 'U.S',
    'Microsoft' : 'U.S',
    'Asus' : 'Taiwan'
}

#딕셔너리 활용해 데이터 프레임의 컬럼에 맵 메서드 수행시키기.
print(df['brand'].map(brand_nation))

df['brand_nation'] = df['brand'].map(brand_nation)

print(df)

#groupby 시작:
print(df.groupby('brand_nation'))
nation_groups = df.groupby('brand_nation')
print(type(nation_groups))
print(nation_groups.count())
nation_groups.plot(kind='box', y='price')
plt.show()