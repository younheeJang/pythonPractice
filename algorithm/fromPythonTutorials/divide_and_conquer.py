def binary_search(list, value):
    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size

    while idx0 <= idxn:
        midIdx = (idx0 + idxn) // 2
        if list[midIdx] == value:
            return midIdx
        if list[midIdx] < value:
            idx0 = midIdx + 1
        else:
            idxn = midIdx - 1
    return None

print(binary_search([1, 5, 9, 16, 78, 999], -99))


def binary_search_recursion(list, idx0, idxn, value):

    if idx0 > idxn:
        return None
    else:
        midIdx = idx0 + (idxn - idx0) // 2
        if list[midIdx] == value:
            return midIdx
        if list[midIdx] < value:
            return binary_search_recursion(list, midIdx + 1, idxn, value)
        else:
            return binary_search_recursion(list, idx0, midIdx-1, value)
    return None

print(binary_search_recursion([1, 5, 9, 16, 78, 999], 0,  len([1, 5, 9, 16, 78, 999])-1, 9))
