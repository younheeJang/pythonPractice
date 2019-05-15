import collections

dictionary1 = {'day1': 'Mon', 'day2': 'Tue'}
dictionary2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dictionary1, dictionary2)

print(res, '\n')
print(res.maps, '\n')
print(format(list(res.keys())))
print()
print(format(list(res.values())))
print()

for k, v in res.items():
    print(k,v)
    print('{}={}'.format(k,v))
    print()


print('day3 in res:{}'.format(('day3' in res)))