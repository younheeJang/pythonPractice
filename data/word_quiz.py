vocabulary = open('files/vocabulary.txt', 'r', encoding="utf-8")

english_word = ''
korean_word = ''
for l in vocabulary:
    english_word = l.strip().split(': ')[0]
    korean_word = l.strip().split(': ')[1]
    guess = input("%s: " % korean_word)
    answer = english_word
    if (guess == answer):
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % answer)

vocabulary.close()

