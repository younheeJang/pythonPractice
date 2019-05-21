list = [64, 34, 25, 12, 22, 11, 90]

def merge_sort(list):
    print(list)
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left_side = list[:middle]
    right_side = list[middle:]
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    return merge(left_side, right_side)


def merge(left_list, right_list):
    res = []
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            res.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list) == 0:
        res = res + right_list
    else:
        res = res + left_list
    return res

print(merge_sort(list))







