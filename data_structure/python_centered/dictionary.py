dictionary01 = {'Name': 'curious', 'Age': 70, 'Class': 'physical'}
dictionary02 = {'Name': 'curious', 'Age': 70, 'Class': 'physical'}
dictionary03 = {'Name': 'curious', 'Age': 70, 'Class': 'physical'}

print ("dictionary01['Name']: ", dictionary01['Name'])
print ("dictionary01['Age']: ", dictionary01['Age'])

dictionary01['Class'] = "english"
print(dictionary01['Class'])


#모든 엔트리를 지워 줌
dictionary03.clear()
print(dictionary03)


#아예 딕셔너리 자체를 지움
del dictionary02
print(dictionary02)