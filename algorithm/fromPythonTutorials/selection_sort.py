def selection_sort(list):
    for index in range(len(list)):
        minimun_index = index
        for next_index in range(index + 1, len(list)):
            if list[minimun_index] > list[next_index]:
                minimun_index = next_index
        list[index], list[minimun_index] = list[minimun_index], list[index]
    return list


l = [19, 2, 31, 45, 30, 11, 121, 27]
selection_sort(l)
print(l)

