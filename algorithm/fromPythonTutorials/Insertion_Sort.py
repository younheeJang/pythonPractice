list = [19, 2, 31, 45, 30, 11, 121, 27]

def insertion_sort(list):
    for index in range(1, len(list)):
        pre_index = index - 1
        next_element = list[index]
        while list[pre_index] > next_element and pre_index >= 0:
            list[pre_index + 1] = list[pre_index]
            pre_index = pre_index - 1
        list[pre_index + 1] = next_element
    return list

list = insertion_sort(list)
print(list)