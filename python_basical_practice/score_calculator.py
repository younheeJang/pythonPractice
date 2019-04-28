def print_grade(midterm, final):
    total = midterm + final
    if total >= 90:
        print('You get an A')
    elif total >= 80:
        print('You get a B')
    elif total >= 70:
        print('You get a C')
    elif total >= 60:
        print('You get a D')
    else:
        print('You fail')

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)