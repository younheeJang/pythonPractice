
def multiple_calculate(num):
    i = 1
    while i < num + 1:
        j = 1
        while j < num + 1:
            print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))
            j += 1
        i += 1


multiple_calculate(9)


