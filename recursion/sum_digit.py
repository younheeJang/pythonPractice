# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    if len(str(n)) == 1:
        return n
    plus = int(n%10)
    n = int(n/10)
    print(plus, n)
    return plus + sum_digits(n)




print(sum_digits(25))
print(sum_digits(225))
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(7))
print(sum_digits(3755))