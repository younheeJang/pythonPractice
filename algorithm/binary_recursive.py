def binary_search(element, some_list, start_index, end_index):

    if start_index > end_index:
        return None

    else:
        mid_index = (start_index + end_index) // 2
        if element > some_list[mid_index]:
            return binary_search(element, some_list, mid_index + 1 , end_index)

        elif element < some_list[mid_index]:
            return binary_search(element, some_list, start_index, mid_index - 1)

    return mid_index


my_list = [2, 3, 5, 7, 11]
start_index = 0
end_index = len(my_list) - 1
print(binary_search(2,  my_list, start_index, end_index))
print(binary_search(0,  my_list, start_index, end_index))
print(binary_search(5,  my_list, start_index, end_index))
print(binary_search(3,  my_list, start_index, end_index))
print(binary_search(11, my_list, start_index, end_index))

