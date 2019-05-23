from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('../data/broadcast1.csv', index_col=0)
print(df)

#시리즈별.
kbs = df['KBS']
mbc = df['MBC']
sbs = df['SBS']
cho = df['TV CHOSUN']
jtbc = df['JTBC']
a = df['Channel A']
mbn = df['MBN']
#ax1 = kbs.plot()
#ax2 = mbc.plot()
#ax3 = sbs.plot()
#ax4 = cho.plot()
#ax5 = jtbc.plot()
#ax6 = a.plot()
#ax7 = mbn.plot()

#한 방송사만
#df.plot(y='KBS')

#여러 방송사
#df.plot(y=['KBS', 'JTBC'])

#다른 방법
df[['KBS', 'JTBC']].plot()

#df.plot()
plt.legend(loc='upper left')
plt.show()

#문자에 대한 그래프는 오류가 남.
