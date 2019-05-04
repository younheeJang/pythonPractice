
def get_sales_average(file):
    new_list = []
    amount = 0
    j = 0
    for i in file_contains:
        new_list.append(list(i.strip().split((": "))))
        amount += int(new_list[j][1])
        j = j + 1
    return amount/len(new_list)

file_contains = open('month_sales.txt', 'r', encoding='utf-8')

print(get_sales_average(file_contains))

file_contains.close()

