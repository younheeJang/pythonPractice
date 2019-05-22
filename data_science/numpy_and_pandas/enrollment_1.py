import pandas as pd

df = pd.read_csv('../data/enrollment_1.csv')


#make column on all rows named 'status' and get value for 'allowed'
df['status'] = 'allowed'

print(df)

#step 1 clear: get freshman and put column 'status' not allowed when course name is 'information....."
bool1 = df['year'] == 1
bool2 = df['course name'] == 'information technology'
print(df.loc[bool1 & bool2])

df.loc[bool1 & bool2, ['status']] = 'not allowed'
print(df.loc[bool1 & bool2])


#step 2 clear: find spefied course name called 'commerce', and get foutrh man's info, put status 'not allowed'
bool3 = df['course name'] == 'commerce'
bool4 = df['year'] == 4
print(df[bool3 & bool4])
df.loc[bool3 & bool4, ['status']] = 'not allowed'
print(df[bool3 & bool4])

#step 1 and step 2 result
print(df[df['status'] == 'not allowed'])

course_counts = df['course name'].value_counts()
closed_courses = course_counts[course_counts < 5]
print(df.loc[closed_courses])
print(list(closed_courses.index))

closed_course_list = list(closed_courses.index)

for index, row in df.iterrows():
    for i in closed_course_list:
        if i == row['course name']:
            #print(row['status'])
            df.at[index, 'status'] = 'not allowed'
            #print(row['status'])

print(df)