def linear_search(list, value):
    index = 0
    for index in range(len(list)):
        if list[index] == value:
            return index
        else:
            index += 1
    return None






l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 90))