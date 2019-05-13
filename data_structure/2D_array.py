
dimentional_arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],
				[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]];


def makeLargestHourGlass(init_arr):
    largestSum = -999
    index_list = list(range(1, len(init_arr)-1))
    print(index_list)
    for i in index_list:
        for j in index_list:
            top = sum(init_arr[i-1][j-1:j-1+3])
            mid = init_arr[i][j]
            bottom = sum(init_arr[i+1][j-1:j-1+3])
            hourglass = top + mid + bottom

            if hourglass > largestSum:
                largestSum = hourglass

    return largestSum


print(makeLargestHourGlass(dimentional_arr))

