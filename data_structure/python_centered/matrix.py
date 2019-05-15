from numpy import *
weekTemperatures = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])

print(weekTemperatures)
weekTemperatures02 = reshape(weekTemperatures,(7,5))
print(weekTemperatures02)

making_row = append(weekTemperatures02,[['Avg',12,15,13,11]], axis=0)
print(making_row)

making_col = insert(weekTemperatures02,[5],[[1],[2],[3],[4],[5],[6],[7]],axis=0)
print(making_col)

making_col = delete(making_col, [range(5,12)], 0)
print(making_col)

making_col = delete(making_col,s_[2],1)

print(making_col)