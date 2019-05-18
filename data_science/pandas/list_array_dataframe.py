import pandas as pd
import numpy as np

two_dimensional_list = [['curious', 78, 'ice-cream'], ['jeager', 89, 'juice']]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['curious', 89, 'ice-cream']),
    pd.Series(['jeager', 80, 'juice'])
]

dataframe1 = pd.DataFrame(two_dimensional_list)
dataframe2 = pd.DataFrame(two_dimensional_array)
dataframe3 = pd.DataFrame(list_of_series)

print(dataframe1)
print(dataframe2)
print(dataframe3)