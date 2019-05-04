def save_word():
    english_word = ''
    korean_meaning = ''

    while True:
        english_word = input("영어 단어를 입력하세요: ")
        korean_meaning = input("한국어 뜻을 입력하세요: ")
        if(english_word == 'q' or korean_meaning == 'q'):
            return False

        out_file.write("%s: %s\n" % (english_word, korean_meaning))

    return False

out_file = open('vocabulary.txt', 'w', encoding="utf-8")

save_word()

out_file.close()