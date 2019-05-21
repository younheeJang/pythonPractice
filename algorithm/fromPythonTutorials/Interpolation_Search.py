
def interpolation_search(list, value):
    length = (len(list))
    mim_index = 0
    max_index = length - 1

    while mim_index <= max_index and value >= list[mim_index] and value <= list[max_index]:
        delta = (value - list[mim_index])/(list[max_index] - list[mim_index])
        position = mim_index + int((max_index - mim_index)*delta)
        if (list[position] > value):
            max_index = position - 1
        elif (list[position] < value):
            mim_index = position + 1
        else:
            return position
    return None


l = [2, 6, 11, 19, 27, 31, 45, 121]
print(interpolation_search(l, 121))
print(interpolation_search(l, 11))
print(interpolation_search(l, 1111))