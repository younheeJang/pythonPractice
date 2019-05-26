from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/young_survey.csv', index_col=0)
#음악과 관련된 컬럼
music = df.iloc[:, :18]
print(music)

#모든 컬럼의 연관성
print(df.corr())

#나이에 대한 컬럼만:나이와 가장 많은 연관성이 있는 순서대로 항목을 나열할 수 있다
print(df.corr()['Age'].sort_values(ascending=False))

print()

#아침에 일찍 일어나는 사람들이 좋아하는 음악 장르:
#print(df.corr()['Getting up'].sort_values())
early = df.corr()['Getting up']
print(early[1:19].sort_values(ascending=True))


#악기 시
#df.corr().loc['Musical instruments', 'Writing']
print('악기 시 ----------------------')
musical_instruments = df.corr()['Musical instruments']
print(musical_instruments.sort_values(ascending=False))
#외모 브랜드
#df.corr().loc['Musical instruments', 'Writing']
print('외모 브랜드 ----------------------')
looks = df.corr()['Spending on looks']
print(looks.sort_values(ascending=False))

#메모 새로운 환경
#df.corr().loc['Writing notes', 'New environment']
print('메모 새로운 환경 ----------------------')
notes = df.corr()['Writing notes']
print(notes.sort_values(ascending=False))


#워커홀릭 헬시푸드
#df.corr().loc['Workaholism', 'Healthy eating']
#df.corr().loc['Prioritising workload', 'Healthy eating']
print('워커홀릭 헬시푸드 ----------------------')
work = df.corr()['Workaholism']
print(work.sort_values(ascending=False))


#히트맵:
#sns.heatmap(music.corr())
#plt.show()



