numbers = [2, 4, 6, 8, 10, 12, 14]



def reversed_list(numbers):
    i = 0
    while i < len(numbers):
        left_index = i
        right_index = len(numbers)-(i+1)
        skip_index = int(len(numbers)/2)
        if(i == skip_index):
            return numbers
        temp = numbers[left_index]
        numbers[left_index] = numbers[right_index]
        numbers[right_index] = temp
        i = i + 1

print(reversed_list(numbers))


i = 0
left_index = i
right_index = len(numbers)-(i+1)
skip_index = int(len(numbers)/2)
temp = numbers[left_index]
numbers[left_index] = numbers[right_index]
numbers[right_index] = temp



print("뒤집어진 리스트: " + str(numbers))