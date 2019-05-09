
def divide_list(left, right):
    for le in left:
        for ri in right:
            if(le > ri):
                temp = le
                le = ri
                ri = temp



def cal_list(my_list):
    if len(my_list) > 1:
        left = my_list[:len(my_list) // 2]
        right = my_list[len(my_list) // 2:]
        divide_list(left, right)
        cal_list(left)
        cal_list(right)
    return  my_list

some_list = [11, 3, 6, 4, 18, 88, 23, 63]
print(cal_list(some_list))


def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
    return x

print(mergeSort(some_list))

#반으로 나눈 두 개의 리스트를 인자로 받아, 어느 한 리스트의 길이가 끝이날 때까지 값을 비교하고, 새로운 리스트에는 항상 작은 값을 넣어준다.
def merge(left, right):
    new_list = []
    le = ri = 0
    while le < len(left) and ri < len(right):
        if left[le] < right[ri]:
            new_list.append(left[le])
            le = le + 1
        else:
            new_list.append(right[ri])
            ri = ri + 1
    #어느 한 리스트에 값이 남아있다면, 아래와 같이 이미 생성된 new_list 뒤에 붙여주는 작업을 통해 새롭게 정렬된 리스트를 리턴할 수 있도록 한다.
    if le == len(left):
        new_list = new_list + right[ri:]
    elif ri == len(right):
        new_list = new_list + left[le:]
    return (new_list)

#리턴되는 리스트 길이가 하나일때까지 계속 재귀함수를 호출해줘서 리스트를 분할해야 함.
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)