def fibo(number):
    count = 1
    a = 1
    b = 1
    print(a)
    print(b)
    while count <= 18:
        b = a + b
        a = b - a
        print(b)
        count = count + 1


fibo(20)
