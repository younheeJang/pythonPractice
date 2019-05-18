import pandas as pd

my_list = [
    {'name':'curious', 'hobby':'baseball', 'id':'sjfaldj;ie;'},
    {'name':'jeager', 'hobby':'coke', 'id':'adadfhfadrae'},
    {'name':'cj', 'hobby':'soccer', 'id':'okgerpm;dvg'}
]

dataFrame = pd.DataFrame(my_list)
print(dataFrame)