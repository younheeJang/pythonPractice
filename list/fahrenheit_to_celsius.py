# function that fahrenheit to ceisius.
def fahrenheit_to_celsius(fahrenheit):
    i = 0
    while i < len(fahrenheit):
        fahrenheit[i] = round((fahrenheit[i] - 32) * 5 / 9, 2)
        i = i + 1
    return fahrenheit


#for test print list.
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# for test print f.
print("화씨 온도 리스트: " + str(sample_temperature_list))

# for test print f -> c
print("섭씨 온도 리스트: " + str(fahrenheit_to_celsius(sample_temperature_list)))

