from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/young_survey.csv', index_col=0)

print(df.iloc[:, 140:])
#기본적인 신상정보
basic_info = df.iloc[:, 139:]

#기본적인 통계정보
print(basic_info.describe())

print(basic_info['Gender'].value_counts())
print(basic_info['Handedness'].value_counts())
print(basic_info['Education'].value_counts())

sns.jointplot(data=basic_info, x='Height', y='Weight')



plt.show()



