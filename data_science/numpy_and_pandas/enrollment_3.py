import pandas as pd

df = pd.read_csv('../data/enrollment_3.csv')

print(df)

#rename column: room assignment to room number:
df.rename(columns={'room assignment':'room number'}, inplace=True)
print(df[df['status'] == 'allowed'].sort_values(by='course name'))
without_not = df['status'] == 'allowed'
print(df['room number'].value_counts())


#강의실별 강좌 이름을 리스트로 묶는다

bool0 = df['status'] == 'allowed'
print(df[bool0])
only_allowed = df[bool0]

bool1 = only_allowed['room number'] == 'Auditorium'
bool2 = only_allowed['room number'] == 'Medium room'
bool3 = only_allowed['room number'] == 'Small room'
bool4 = only_allowed['room number'] == 'Large room'
list1 = only_allowed.loc[bool1, 'course name'].unique()
print(list1)
list2 = only_allowed.loc[bool2, 'course name'].unique()
print(list2)
list3 = only_allowed.loc[bool3, 'course name'].unique()
print(list3)
list4 = only_allowed.loc[bool4, 'course name'].unique()
print(list4)



#강의실별 강좌 이름을 알파벳순서로 정렬한다.
sorted1 = sorted(list1)
print(sorted1)

sorted2 = sorted(list2)
print(sorted2)

sorted3 = sorted(list3)
print(sorted3)

sorted4 = sorted(list4)
print(sorted4)

#강의실별 강좌이름을 알파벳순서로 정렬한 리스트 활용 + 포문을 사용해서 , 'room number'컬럼을 바꾼다.

for index, row in df.iterrows():
    number = 1
    for i in sorted3:
        if i == row['course name']:
            df.at[index, 'room number'] = 'Small-' + str(number)
        number += 1
    number = 1
    for i in sorted1:
        if i == row['course name']:
            df.at[index, 'room number'] = 'Auditorium-' + str(number)
        number += 1
    number = 1
    for i in sorted2:
        if i == row['course name']:
            df.at[index, 'room number'] = 'Medium-' + str(number)
        number += 1
    number = 1
    for i in sorted4:
        if i == row['course name']:
            df.at[index, 'room number'] = 'Large-' + str(number)
        number += 1

    if row['status'] == 'not allowed':
        df.at[index, 'room number'] = 'not assigned'



print(df)
