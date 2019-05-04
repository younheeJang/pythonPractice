from random import randint
vocab = open('files/vocabulary.txt', 'r', encoding="utf-8")

#step1:make dictionary from file values.
dict = {}
for i in vocab:
    dict[i.strip().split(': ')[0]] = i.strip().split(': ')[1]
print(dict)

#step2:



#keys = list(vocab.keys())

