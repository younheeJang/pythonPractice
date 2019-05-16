import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000,
    440000, 140000, 180000, 340000,
    330000, 290000, 280000, 380000,
    400000, 350000, 380000, 150000,
    110000, 240000, 380000, 380000,
    340000, 420000, 150000, 130000
]

# 코드를 작성하세요.

# 정답 출력
revenue_in_yen = np.array(revenue_in_yen)
booleans = revenue_in_yen > 300000

print(booleans)

filter = np.where(booleans)
print(filter)
bad_days_revenue = revenue_in_yen[filter]
print(bad_days_revenue)