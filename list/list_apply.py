# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
# 코드를 입력하세요
i = 1
while i <= 10:
    numbers.append(i)
    i = i + 1

print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
evenList = []
oddList = []
while i < len(numbers):
    if(i%2):
        evenList.append(numbers[i])
    else:
        oddList.append(numbers[i])
    i = i + 1

i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        print(numbers[i])
        del numbers[i]
    i += 1

numbers.insert(0,20)
numbers.sort()

print(numbers)

def your_request(length, input_later):
    #step1: make list accept user's want
    i = 1
    res = []
    while i <= length:
        res.append(i)
        i = i + 1
    print(res)

    #step2: remain even not odd
    i = 0
    while i < len(res):
        if res[i] % 2 != 0:
            del res[i]
        i += 1
    print(res)

    #step3: insert input_later and sort
    res.insert(0, input_later)
    print(res)

    res.sort()

    return res

print(your_request(10, 20))