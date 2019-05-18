import numpy as np
import pandas as pd

names = ['curious', 'jeager', 'juice']
hobby = ['soccer', 'baseball', 'drinking']
birth = ['12548452', '16547895', '41254785']

dict1 = {
    'name':names,
    'hobby':hobby,
    'birth':birth
}

np_arr = np.array(dict1)

print(np_arr)

dict2 = {
    'name':np.array(names),
    'hobby':np.array(hobby),
    'birth':np.array(birth)
}

np_arr2 = dict2
print(np_arr2)


dict3 = {
    'name':pd.Series(names),
    'hobby':pd.Series(hobby),
    'birth':pd.Series(birth)
}

np_arr3 = dict3
print(np_arr3)

dataframe1 = pd.DataFrame(dict1)
dataframe2 = pd.DataFrame(dict2)
dataframe3 = pd.DataFrame(dict3)

print(dataframe1)
print(dataframe2)
print(dataframe3)