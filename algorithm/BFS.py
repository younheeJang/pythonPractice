from collections import deque

# 지하철역 클래스
class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)


# Breadth-First Search 알고리즘
def bfs(start, goal):
    # 변수 정의
    prev = {}
    queue = deque()
    curr = None

    # 초기 설정
    prev[start] = None
    queue.append(start)


    # 탐색
    while len(queue) > 0 and curr != goal:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in prev.keys():
                queue.append(neighbor)
                prev[neighbor] = curr
    # 길이 있으면 경로를 만들어서 리턴
    if curr == goal:
        path = [goal]
        x = goal

        while prev[x] != None:
            x = prev[x]
            path.append(x)

        return path

    # 길이 없으면 None 리턴
    return None

#지하철 노선도 그리기
def make_station_road(in_file):
    for line in in_file:
        previous_station = None
        data = line.strip().split("-")
        for name in data:
            station_name = name.strip()
            if station_name not in stations.keys():
                current_station = Station(station_name)
                stations[station_name] = current_station
            else:
                current_station = stations[station_name]
            if previous_station != None:
                current_station.add_connection(previous_station)

            previous_station = current_station

# 파일 읽기
stations = {}
in_file = open('data/stations.txt', 'r', encoding='utf-8')

make_station_road(in_file)

in_file.close()


# 테스트
start_name = "산본"
goal_name = "범계"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)