


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

save_word()

