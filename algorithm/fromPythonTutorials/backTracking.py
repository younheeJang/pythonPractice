def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]


def except_particular_value(value):
    if value in permute(2, ["a", "b", "c"]):
        return value
    else:
        return None


print(permute(2, ["a", "b", "c"]))
value = 'aa'
print(except_particular_value(value))