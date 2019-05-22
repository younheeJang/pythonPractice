import pandas as pd

df = pd.read_csv('../data/enrollment_1.csv')
df['status'] = 'allowed'

# 코드를 작성하세요.
#step 1 clear: get freshman and put column 'status' not allowed when course name is 'information....."
bool1 = df['year'] == 1
bool2 = df['course name'] == 'information technology'

df.loc[bool1 & bool2, 'status'] = 'not allowed'


#step 2 clear: find spefied course name called 'commerce', and get foutrh man's info, put status 'not allowed'
bool3 = df['course name'] == 'commerce'
bool4 = df['year'] == 4

df.loc[bool3 & bool4, 'status'] = 'not allowed'

# 정답 출력
print(df)