startHour = [[13,15,17], [10,13], [9,16,18]]

print(startHour)
print(startHour[0])
print(startHour[0][2])

for row in startHour:
    for col in row:
        print(col, end=" ")
    print()

startHour.insert(2, [11, 15, 19])
print(startHour)

startHour[2] = [6, 18]
startHour[0][0] = 1
print(startHour)

del startHour[1]
print(startHour)