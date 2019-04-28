PERIOD = 2016 - 1988
MONEY = 50000000
INTEREST_RATE = 0.12
res = 0
who = ''

def if_bank(MONEY, PERIOD):
    year = 1
    while year <= PERIOD:
        MONEY = MONEY * (1 + INTEREST_RATE)
        year += 1
    return int(MONEY)

def if_apartment():
    return 1100000000

def bank_apartment_response(b, a):
    if b < a:
        res = a - b
        who = '미란 아주머니'
    elif b > a:
        res = b - a
        who = '동일 아저씨'
    return str(res)+'원 차이로 '+who+'의 말씀이 맞습니다.'


print(bank_apartment_response(if_bank(MONEY, PERIOD), if_apartment()))