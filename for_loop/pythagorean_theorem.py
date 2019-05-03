def pythagorean_theorem():
    for a in range(1, 333):
        for b in range(a + 1, 500):
            c = 1000 - a - b
            if a < b < c:
                print(a, b, c)
                if a ** 2 + b ** 2 == c ** 2:
                    print(a ** 2, b ** 2, c ** 2)
                    print(a * b * c)
                    return False



pythagorean_theorem()


def pythagorean_theorem():
    for a in range(1, 333):
        for b in range(a + 1, 500):
            c = 1000 - a - b
            if a < b < c:
                if a ** 2 + b ** 2 == c ** 2:
                    return a * b * c


print(pythagorean_theorem())
