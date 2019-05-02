from random import randint

numbers = []

# 세개 뽑을때까지 반복
while len(numbers) < 3:
    new_number = randint(0, 9)

    # 새로운 수 나올때까지 다시 뽑기
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

print(numbers)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")


count = 0
user_input = []
while count < 3:
    count = count + 1
    u_input = int(input("%s번째 수를 입력하세요: " % count))
    while u_input in user_input:
        print("중복되는 수 입니다. 다시 입력해주세요.")
        u_input = int(input("%s번째 수를 입력하세요: " % count))
    while u_input > 9 or u_input < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        u_input = int(input("%s번째 수를 입력하세요: " % count))
    user_input.append(u_input)


print(user_input)


