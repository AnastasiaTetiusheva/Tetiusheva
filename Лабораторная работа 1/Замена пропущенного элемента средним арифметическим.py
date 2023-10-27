numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
len_of_numbers = len(numbers)
sum_of_numbers_1 = sum(numbers[:4])
summ_of_numbers_2 = sum(numbers[5:])
average_of_numbers = (sum_of_numbers_1+summ_of_numbers_2)/len_of_numbers
numbers[4] = average_of_numbers

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
