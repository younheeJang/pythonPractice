# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    standard = len(str(num))
    i = 0
    sum = 0
    while i < standard:
        plusNumber = int(num % 10)
        num = int(num / 10)
        i = i + 1
        sum = sum + plusNumber
    return sum

#원하는 수를 입력받아 리턴.
def get_sum_digit(num):
    sum = 0
    for n in list(range(1, num+1)):
        sum = sum + sum_digit(n)
    return sum

print(get_sum_digit(1000))
