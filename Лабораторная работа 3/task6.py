list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_in_list = max(list_numbers)
i= 0
while list_numbers[i] != max_in_list:
    i += 1
last_in_list = list_numbers[-1]
list_numbers[i] = last_in_list
list_numbers[-1] = max_in_list
print(list_numbers)
