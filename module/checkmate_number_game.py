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
            print('%s    %s' % (used_oppertunity, oppertunity))
            if(oppertunity==0):
                print('아쉽습니다. 정답은 %d였습니다.' % (com_answer))
                return False
            else:
                answer = int(input('기회가 %d번 남았습니다. %s' % (oppertunity, QUESTION)))
        elif (answer > com_answer):
            print('Down')
            oppertunity = oppertunity - used_oppertunity
            print('%s    %s' % (used_oppertunity, oppertunity))
            if (oppertunity == 0):
                print('아쉽습니다. 정답은 %d였습니다.' % (com_answer))
                return False
            else:
                answer = int(input('기회가 %d번 남았습니다. %s' % (oppertunity, QUESTION)))

#checkmate_number_game(12, 4)

checkmate_number_game(randint(1, 20), 4)

