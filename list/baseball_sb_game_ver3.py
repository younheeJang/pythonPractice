from random import randint

# make number array length 2 not same:
def get_winning_numbers():
    numbers = []

    while len(numbers) < 3:
        new_number = randint(0, 9)

        while new_number in numbers:
            new_number = randint(0, 9)
        numbers.append(new_number)
    return numbers

def get_user_numbers():
    # make number array from user's input and value should not same, not out of range:
    user_input = []
    while  len(user_input) < 3:
        u_input = int(input("%s번째 수를 입력하세요: " % str(len(user_input)+1)))
        if u_input in user_input:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        if u_input > 9 or u_input < 0:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue
        user_input.append(u_input)
    return user_input

def count_strike_and_ball(numbers, user_input):
    # count strike and ball:
    index = 0
    strike = 0
    ball = 0
    while index < 3:
        if user_input[index] == numbers[index]:
            strike += 1
        elif user_input[index] in numbers:
            ball += 1
        index = index + 1
    return strike, ball


def get_result(strike, ball):
    how_many_users_tried = 1
    if (strike == 3):
        print("%dS %dB" % (strike, ball))
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % how_many_users_tried)
        return False
    print("%dS %dB" % (strike, ball))
    how_many_users_tried += 1

def baseball_3Strik_game():

    numbers = get_winning_numbers()

    while True:

        # start game:
        print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
        print("세 수를 하나씩 차례대로 입력하세요.")

        user_input = get_user_numbers()

        result = count_strike_and_ball(numbers, user_input)

        result = get_result(result[0], result[1])
        if(result == False):
            return False


baseball_3Strik_game()