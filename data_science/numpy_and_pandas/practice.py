from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/sillicon_valley_detail.csv', index_col='company')



bool0 = df['company'] == 'Adobe'

#인원이 0인 직군은 뺀다.
bool1 = df['count'] == 0

forChart = df[~bool1 & bool0]
print(forChart)

#한 회사만 차트에 반영할 것이므로 필요 로우만 추리기

#forChart = forChart.loc['Adobe']


#label로 설정할 컬럼 중 필요없는 항목을 걸러내기 위해 조건을 설정하기.
bool2 = (forChart['job_category'] != 'Totals') & (forChart['job_category'] != 'Previous_totals')

forChart = forChart[bool2]


#걸러낸 항목 중 인종별로 토털을 기록한 항목이 있음. 걸러냄.

forChart = forChart[forChart['race'] == 'Overall_totals']

#필요없는 컬럼은 지운다.
forChart = forChart.drop(['race', 'gender', 'year'], axis=1)



#걸러낸 데이터 프레임을 활용해 차트를 그림
#forChart.plot(kind='pie', labels=forChart['job_category'], y='count')