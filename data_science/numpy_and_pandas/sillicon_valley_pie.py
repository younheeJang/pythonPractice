from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/sillicon_valley_detail.csv', index_col='company')
print(df)
#인원이 0인 직군은 뺀다.
bool1 = df['count'] == 0
print(df[~bool1])
forChart = df[~bool1]
print(forChart)

#한 회사만 차트에 반영할 것이므로 필요 로우만 추리기
print(forChart.loc['Adobe'])
forChart = forChart.loc['Adobe']

#totals previous_totals 거르기.
#bool2 = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')
#print(df[bool2])

#label로 설정할 컬럼 중 필요없는 항목을 걸러내기 위해 조건을 설정하기.
bool2 = (forChart['job_category'] != 'Totals') & (forChart['job_category'] != 'Previous_totals')
print(forChart[bool2])
forChart = forChart[bool2]
#print(forChart[forChart['job_category'] == 'Totals'])

#걸러낸 항목 중 인종별로 토털을 기록한 항목이 있음. 걸러냄.
print(forChart[forChart['race'] == 'Overall_totals'])
forChart = forChart[forChart['race'] == 'Overall_totals']

#필요없는 컬럼은 지운다.
forChart = forChart.drop(['race', 'gender', 'year'], axis=1)
print(type(forChart))
print(forChart.set_index('job_category'))
forChart = forChart.set_index('job_category')
#걸러낸 데이터 프레임을 활용해 차트를 그림
#forChart.plot(kind='pie', labels=forChart['job_category'], y='count')
forChart.plot(kind='pie',  y='count')
plt.legend(loc='upper left')
plt.show()




#forChart.Data.plot(kind='pie')
#print(forChart.columns)
#print(forChart)
#필요없는 컬럼 지우기
#print(forChart.drop(['race', 'gender', 'year'], axis=1))
#forChart = forChart.drop(['race', 'gender', 'year'], axis=1)

#print(forChart['job_category'].unique())
#forChart['job_category'].plot.pie(subplots=True, y='count')
#forChart.plot(kind='pie', labels=forChart['job_category'], y='count')
#plt.legend(loc='upper left')
#plt.show()

