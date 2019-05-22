import pandas as pd

df = pd.read_csv('../data/enrollment_2.csv')

#basic settings
df['room assignment'] = 'Auditorium'
print(df)

print()
#processing not allowed / not assigned
df.loc[df['status'] == 'not allowed', 'room assignment'] = 'not assigned'
print(df)

#print(df.sort_values(by="course name"))
course_counts = df['course name'].value_counts()
closed = df['status'] == 'not allowed'
print(df[closed])
bool80 = df['course name'].value_counts() >= 80
bool40 = df['course name'].value_counts() >= 40
bool15 = df['course name'].value_counts() >= 15
bool05 = df['course name'].value_counts() >= 5
print(course_counts[bool80])
print(course_counts[~bool80 & bool40])
print(course_counts[~bool80 & ~bool40 & bool15])
print(course_counts[~bool80 & ~bool40 & ~bool15 & bool05])

over80 = list(course_counts[bool80].index)
print(over80)

over40 = list(course_counts[~bool80 & bool40].index)
print(over40)

over15 = list(course_counts[~bool80 & ~bool40 & bool15].index)
print(over15)

over05 = list(course_counts[~bool80 & ~bool40 & ~bool15 & bool05].index)
print(over05)



for index, row in df.iterrows():
    for i in over80:
        if i == row['course name']:
            df.at[index, 'room assignment'] = 'Auditorium'

    for i in over40:
        if i == row['course name']:
            df.at[index, 'room assignment'] = 'Large room'

    for i in over15:
        if i == row['course name']:
            df.at[index, 'room assignment'] = 'Medium room'

    for i in over05:
        if i == row['course name']:
            df.at[index, 'room assignment'] = 'Small room'

    if row['status'] == 'not allowed':
        df.at[index, 'room assignment'] = 'not assigned'


print(df)