from random import randint

#print(randint(1,20))

def checkmate_number_game(com_answer, OPPERTUNITY):
    count = 0
    used_oppertunity = 1
    QUESTION = '1-20 사이의 숫자를 맞춰보세요: '
    oppertunity = OPPERTUNITY
    answer = int(input('기회가 %d번 남았습니다. %s' % (OPPERTUNITY, QUESTION)))
    while used_oppertunity <= OPPERTUNITY:
        if(answer == com_answer):
            count = (OPPERTUNITY + 1) - oppertunity
            print('축하합니다. %d번만에 숫자를 맞추셨습니다.' % (count))
            return False
        elif(answer < com_answer):
            print('Up')
            oppertunity = oppertunity - used_oppertunity
            #print('%s    %s' % (used_oppertunity, oppertunity))
            if(oppertunity==0):
                print('아쉽습니다. 정답은 %d였습니다.' % (com_answer))
                return False
            else:
                answer = int(input('기회가 %d번 남았습니다. %s' % (oppertunity, QUESTION)))
        elif (answer > com_answer):
            print('Down')
            oppertunity = oppertunity - used_oppertunity
            #print('%s    %s' % (used_oppertunity, oppertunity))
            if (oppertunity == 0):
                print('아쉽습니다. 정답은 %d였습니다.' % (com_answer))
                return False
            else:
                answer = int(input('기회가 %d번 남았습니다. %s' % (oppertunity, QUESTION)))

#checkmate_number_game(12, 4)

#checkmate_number_game(randint(1, 20), 4)


#guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % tries))

#if ANSWER > guess:
#    print("Up")
#elif ANSWER < guess:
#    print("Down")
#else:
#    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - tries))
#    break

def checkmate_selected_number(number, oppertunity):
    tries = 1
    while tries <= oppertunity:
        guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % ((oppertunity+1) - tries)))
        if guess == number:
            print('축하합니다. %d번만에 숫자를 맞추셨습니다.' % tries)
            return False
        elif guess < number:
            print('Up')
        else:
            print('Down')
        tries = tries + 1
    print('아쉽습니다. 정답은 %d였습니다.' % (number))
    return False

checkmate_selected_number(randint(1,20),4)