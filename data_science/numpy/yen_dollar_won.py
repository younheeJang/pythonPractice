import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000,
    440000, 140000, 180000, 340000,
    330000, 290000, 280000, 380000,
    170000, 140000, 230000, 390000,
    400000, 350000, 380000, 150000,
    110000, 240000, 380000, 380000,
    340000, 420000, 150000, 130000,
    360000, 320000, 250000
]

revenue_in_dollar = [
    1200, 1600, 1400, 1300,
    2100, 1400, 1500, 2100,
    1500, 1500, 2300, 2100,
    2800, 2600, 1700, 1400,
    2100, 2300, 1600, 1800,
    2200, 2400, 2100, 2800,
    1900, 2100, 1800, 2200,
    2100, 1600, 1800
]

# 코드를 작성하세요.
revenue_in_yen = np.array(revenue_in_yen)
revenue_in_yen = revenue_in_yen * 10.08
revenue_in_dollar = np.array(revenue_in_dollar)
revenue_in_dollar = revenue_in_dollar * 1138
# 정답 출력
won_array = revenue_in_yen + revenue_in_dollar
print(won_array)