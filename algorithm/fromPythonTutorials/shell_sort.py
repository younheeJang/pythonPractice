def shell_sort(list):
    sublistcount = len(list)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_Insertion_sort(list, start_position, sublistcount)
      print(sublistcount, " ",list)
      sublistcount = sublistcount // 2

def gap_Insertion_sort(list,start,gap):
    for i in range(start+gap,len(list),gap):
        current_value = list[i]
        #print(current_value)
        position = i

        while position >= gap and list[position-gap] > current_value:
            #print('  '+str(nlist[position-gap]))
            list[position] = list[position-gap]
            position = position-gap

        list[position] = current_value



list = [14,76,43,27,57,13,45,21,70]

print(list)
shell_sort(list)
print(list)