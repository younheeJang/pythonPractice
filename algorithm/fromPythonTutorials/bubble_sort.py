list = [19, 2, 31, 45, 6, 11, 121, 27]


def bubble_sorting(list):
    print(list)
    for numeric_items in range(len(list)-1, 0, -1):
        for index in range(numeric_items):
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp
    return list

print(bubble_sorting(list))




list2 = [19, 2, 31, 45, 6, 11, 121, 27]

def bubble_sorting2(list):
    print(list)
    for numeric_items in range(len(list)-1, 0, -1):
        for index in range(numeric_items):
            if list[index] > list[index+1]:
                list[index], list[index + 1] = list[index + 1], list[index]
    return list

print(bubble_sorting2(list2))