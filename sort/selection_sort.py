# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.
    for index_x in range(len(my_list)):
        minimum_index = index_x
        for index_y in range(index_x + 1, len(my_list)):
            if my_list[index_x] > my_list[index_y]:
                temp = my_list[index_x]
                my_list[index_x] = my_list[index_y]
                my_list[index_y] = temp
                print(my_list)
    return my_list

some_list = [1, 21, 51, 84, 954, 12]
print(selection_sort(some_list))

print('----------------')

# 선택 정렬
def selection_sort_ver2(my_list):
    # 코드를 입력하세요.
    for index_x in range(len(my_list)):
        minimum_index = index_x
        for index_y in range(index_x + 1, len(my_list)):
            if my_list[index_x] > my_list[index_y]:
                index_x = index_y
                print(my_list)
        my_list[index_x], my_list[minimum_index] = my_list[minimum_index], my_list[index_x]
    return my_list

some_list = [1, 21, 51, 84, 954, 12]
print(selection_sort_ver2(some_list))
