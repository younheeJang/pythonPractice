i = 1
while i <= 100:
    if ((i%8==0) and (i%12!=0)):
        print(i)
    i = i+1

i = 1
res = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        res = res + i
    i += 1
print(res)

n = 120

def get_devided_number(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            print(i)
            count += 1
        i += 1
    print(str(n)+'의 약수는 총 '+str(count)+'개입니다.')

get_devided_number(n)

