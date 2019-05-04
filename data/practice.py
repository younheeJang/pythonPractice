


def save_word():
    english_word = ''
    korean_word = ''

    while True:
        english_word = input("영어 단어를 입력하세요: ")
        korean_word = input("한국어 뜻을 입력하세요: ")
        if(english_word == 'q' or korean_word == 'q'):
            return False

    print("%s: %s" % (english_word, korean_word))

    return False

#save_word()



print("맞았습니다!")
print("아쉽습니다. 정답은 OOO입니다.")

korean_word = '고양이'

guess = input("%s: " % korean_word)

answer = 'cat'
if(guess == answer):
    print("맞았습니다!")
else:
    print("아쉽습니다. 정답은 %s입니다." % answer)
