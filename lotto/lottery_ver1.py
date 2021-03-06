from random import randint

#겹치지 않도록 숫자 여섯 개 리스트 리턴
def generate_numbers():

    lotto_numbers = []

    i = 0
    lotto_number = 0
    while len(lotto_numbers) < 6:
        lotto_number = randint(1, 45)
        while lotto_number in lotto_numbers:
            lotto_number = randint(1, 45)
        lotto_numbers.append(lotto_number)
    lotto_numbers = sorted(lotto_numbers)
    return lotto_numbers

print(generate_numbers())

def draw_winning_numbers():

    winning_numbers = generate_numbers()
    winning_number = randint(1, 45)
    while winning_number in winning_numbers:
        winning_number = randint(1, 45)
    winning_numbers.append(winning_number)
    return winning_numbers

print(draw_winning_numbers())


def count_matching_numbers1(list1, list2):
    count = 0
    for list_n1 in list1:
        for list_n2 in list2:
            if(list_n1 == list_n2):
                count += 1
    return count


def count_matching_numbers(list1, list2):
    count = 0
    for list_n1 in list1:
        if(list_n1 in list2):
                count += 1
    return count


#print(count_matching_numbers([1,2,5,6],[1,25,8,2,9]))
#print(count_matching_numbers(generate_numbers(), generate_numbers()))

def check(numbers, winning_numbers):
    matching_number = count_matching_numbers(numbers, winning_numbers)
    bonus_number = winning_numbers[-1]
    if matching_number == 6 and bonus_number not in numbers:
        return 1000000000
    elif matching_number == 5 and bonus_number in numbers:
        return 50000000
    elif matching_number == 5:
        return 1000000
    elif matching_number == 4:
        return 50000
    elif matching_number == 3:
        return 5000
    else:
        return 0

#print(check(generate_numbers(), draw_winning_numbers()))

#print(check([1,5,7,9,30,36], [1,5,7,9,30,33,36]))

#print(check([1,2,3,4,5,7], [1,2,3,4,5,6,7]))



