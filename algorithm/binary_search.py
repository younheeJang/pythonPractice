def binary_search11(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    while True:
        if start_index > end_index:
            return None
        center_index = (start_index + end_index) // 2
        if (some_list[center_index] < element):
            start_index = center_index + 1
        elif (some_list[center_index] > element):
            end_index = center_index - 1
        elif (some_list[center_index] == element):
            return center_index

#print(binary_search11(2, [2, 3, 5, 7, 11]))
#print(binary_search11(0, [2, 3, 5, 7, 11]))
#print(binary_search11(5, [2, 3, 5, 7, 11]))
#print(binary_search11(3, [2, 3, 5, 7, 11]))
#print(binary_search11(11, [2, 3, 5, 7, 11]))



def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    #시작 인덱스가 마지막 인덱스보다 크지 않을 동안만 반복되면 된다.
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        #이 함수가 끝나려면 여기를 통과하든 반복문을 벗어나 None을 리턴하든 둘 중에 하나.
        if some_list[mid_index] == element:
            return mid_index

        # 지정 숫자가 가운데 인덱스 범위를 안에 있는 경우: 마지막 인덱스를 지정
        elif some_list[mid_index] > element:
            end_index = mid_index - 1

        # 지정 숫자가 가운데 인덱스 범위를 벗어난 경우: 첫 인덱스를 지정
        elif some_list[mid_index] < element:
            start_index = mid_index + 1


print(binary_search(11, [2, 3, 5, 7, 11]))

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))

print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))



