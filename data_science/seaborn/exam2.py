from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/exam.csv', index_col=0)
print(df)

#상관계수를 데이터프레임 형태로 출력
print(df.corr())

#옵션 추가
#sns.heatmap(df.corr())
sns.heatmap(df.corr(),  annot=True)

#색이 밝을 수록 상관 계수가 커지는 히트 맵.


#카테고리별 분류: 카테고리=x
#sns.catplot(data=df, x='smoker', y='charges', kind='violin')

#sns.kdeplot(df['Height'], bw=0.01)
plt.show()



