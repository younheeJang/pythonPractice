file_contains = open('files/sales_list.txt', 'r', encoding='utf-8')
print(file_contains)

for line in file_contains:
    print(line.strip())



file_contains.close()


for line in file_contains:
    print(line.split((',')))

