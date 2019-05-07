vocabulary = open('files/vocabulary.txt', 'r', encoding="utf-8")

#패러미터는, 변수가 사용되기 전에만, 미리 선언되어 있으면 된다.
for voca in vocabulary:
    words = voca.strip().split(': ')
    english_word = words[0]
    korean_word = words[1]
    guess = input("%s: " % korean_word)
    answer = english_word
    if (guess == answer):
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % answer)

vocabulary.close()

