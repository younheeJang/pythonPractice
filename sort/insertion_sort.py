def insertion_sort(arr):
    # 삽입정렬할 리스트를 차례로 돌림.
    for i in range(1, len(arr)):

        # 맨 처음 인덱스 바로 뒤의 값을 키로 갖고 들어감.
        key = arr[i]

        # 바로 앞의 값에 접근할 수 있도록 인덱스로 사용할 변수 하나를 만든다.
        j = i - 1

        # 지정된 범위(j >= 0 )안에 확실히 있으며, 뒤의 수(key)가 앞의 수(arr[j])보다 작은 동안 계속.
        while j >= 0 and key < arr[j]:
            # 뒤의 작은 수를 바로 앞의 큰 수와 바꿔준다.
            arr[j + 1] = arr[j]
            # 그리고, 그 비교를 인덱스가 0이 될 때까지 반복한다.
            j -= 1
        # i를 주축으로 한번 도는 포문을 지날 때마다, key값을 정리해준다. key를 중심으로 비교를 하기 떄문에 이 코드가 없으면
        # key값 때문에 엉킨다.
        arr[j + 1] = key
        print(arr[j+1])
    return arr


arr = [8, 3, 1, 2]
print(arr)
print(insertion_sort(arr))
