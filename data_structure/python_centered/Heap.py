import heapq

#H = [21, 1, 45, 78, 3, 5]
H = [1, 2, 3, 4]

#Min-heap힙으로 바꾼다
heapq.heapify(H)
print(H)

#값 푸시
heapq.heappush(H, 8)
print(H)

#인덱스 포지션 1에 있는 값을 지움
heapq.heappop(H)
print(H)

#가장 작은 요소를 지우고 대체.
heapq.heapreplace(H, 6)
print(H)

heapq.heapify(H)
print(H)

