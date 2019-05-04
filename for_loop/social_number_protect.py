def mask_security_number(security_number):
    # 코드를 입력하세요.
    i = 0
    list_to_string = ''
    num_list = list(security_number)
    while i < 4:
        num_list[(len(num_list)-1)-i] = '*'
        i = i + 1
    for l in num_list:
        list_to_string += l
    return list_to_string

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))