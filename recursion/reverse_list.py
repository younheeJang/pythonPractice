def flip(some_list):
    if not some_list: return []
    return [some_list[-1]] + flip(some_list[:-1])



# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flip(some_list))
print(some_list[:-1])
def flip01(some_list):
    # 코드를 입력하세요.
    endNumber = int(len(some_list) / 2)
    index = 0
    while index < endNumber:
        print(some_list)
        index += 1
def flip02(some_list):
    if not some_list: return []
    return [some_list[-1]] + flip(some_list[:-1])
