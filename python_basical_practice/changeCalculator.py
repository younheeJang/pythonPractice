def calculate_change(payment, cost):
    res = payment - cost
    fif10 = res // 1000 // 50
    one10 = ((res // 1000 - 50 * fif10) // 10)
    fif = ((res // 1000 - 50 * fif10) % 10)
    getFif = fif // 5
    getOne = fif - getFif * 5

    # print(res)
    # print(fif10, one10, fif)
    print('50000원 지폐: %d장' % (fif10))
    print('10000원 지폐: %d장' % (one10))
    print('5000원 지폐: %d장' % (getFif))
    print('1000원 지폐: %d장' % (getOne))


# 테스트
calculate_change(100000, 1000)
print()
calculate_change(500000, 377000)