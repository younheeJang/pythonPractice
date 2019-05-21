import pandas as pd

#인덱스 컬럼 0으로 놓고
body_info = pd.read_csv('../data/body_info.csv', index_col=0)
print(body_info)

#NaN을 200.000000으로 변경
body_info.iloc[1, 1] = 200.000000
print(body_info.iloc[1, 1])
print(body_info)

#로우 21 삭제
#body_info.drop(body_info['ID'] == 21, axis="index", inplace=True)
#bool1 = body_info['ID'] == 21
body_info.drop(21, axis='index', inplace=True)
print(body_info)

#ID 20의 로우 추가.
body_info.loc[20] = [70, 200]
print(body_info)




