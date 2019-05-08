from random import randint
vocab = open('files/vocabulary.txt', 'r', encoding="utf-8")

#step1:make dictionary from file values.
words = {}
for index in vocab:
    korean_word = index.strip().split(': ')[1]
    english_word = index.strip().split(': ')[0]
    words[korean_word] = english_word
keys = list(words.keys())


#step2:

while True:
    index = randint(0, len(keys)-1)
    answer = input('%s: ' % keys[index])
    if(answer == words[keys[index]]):
        print('맞았습니다!')
    elif(answer == 'q'):
        break
    else:
        print('틀렸습니다. 정답은 %s입니다.' % words[keys[index]])


vocab.close()