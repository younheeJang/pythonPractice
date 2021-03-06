from random import randint

#겹치지 않도록 숫자 여섯 개 리스트 리턴하는 함수
def generate_numbers():

    lotto_numbers = []

    lotto_number = 0
    while len(lotto_numbers) < 6:
        lotto_number = randint(1, 45)
        while lotto_number in lotto_numbers:
            lotto_number = randint(1, 45)
        lotto_numbers.append(lotto_number)
    lotto_numbers = sorted(lotto_numbers)
    return lotto_numbers


#로또 기계가 뽑는 겹치지 않는 6개의 숫자 + 보너스 숫자 생성해 리턴하는 함수
def draw_winning_numbers():

    winning_numbers = generate_numbers()
    winning_number = randint(1, 45)
    while winning_number in winning_numbers:
        winning_number = randint(1, 45)
    winning_numbers.append(winning_number)
    return winning_numbers


#사용자의 숫자 여섯 개와 로또 기계가 뽑은 숫자 총 일곱개를 인자로 받아 매칭되는 숫자의
#개수를 리턴하는 함수
def count_matching_numbers(list1, list2):
    count = 0
    for list_n1 in list1:
        if(list_n1 in list2):
                count += 1
    return count


#print(count_matching_numbers([1,2,5,6],[1,25,8,2,9]))
#print(count_matching_numbers(generate_numbers(), generate_numbers()))

#돈으로 환산해 리턴하는 함수
def check(numbers, winning_numbers):

    #일반번호 6개, 보너스번호 1개, 매칭되는 넘버를 담을 변수 선언 및 세팅.
    only_general_numbers = winning_numbers[:6]
    bonus_number = winning_numbers[-1]
    matching_number = count_matching_numbers(numbers, only_general_numbers)

    #내가 뽑은 번호 6개와 일반 번호 6개 모두 일치 (10억원)
    if matching_number == 6 and bonus_number not in numbers:
        return 1000000000

    #내가 뽑은 번호 5개와 일반 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만원)
    elif matching_number == 5 and bonus_number in numbers:
        return 50000000

    #내가 뽑은 번호 5개와 일반 번호 5개 일치 (100만원)
    elif matching_number == 5:
        return 1000000

    #내가 뽑은 번호 4개와 일반 번호 4개 일치 (5만원)
    elif matching_number == 4:
        return 50000

    #내가 뽑은 번호 3개와 일반 번호 3개 일치 (5천원)
    elif matching_number == 3:
        return 5000

    else:
        return 0

#print(check(generate_numbers(), draw_winning_numbers()))

#print(check([1,5,7,9,30,36], [1,5,7,9,30,33,36]))

#print(check([1,2,3,4,5,7], [1,2,3,4,5,6,7]))

#print(check([1,2,3,4,5,6], [1,2,7, 8, 9, 10, 3]))



