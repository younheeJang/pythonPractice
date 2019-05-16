import pandas as pd

two_dimentional_list = [['curious', 88, 12351555], ['jeager', 89, 84223644]]

pd_list = pd.DataFrame(two_dimentional_list, columns=['name', 'birth', 'id'], index=['a', 'b'])

print(pd_list)
print(pd_list.dtypes)