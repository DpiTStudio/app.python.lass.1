first_number = 123
second_number = 904

last_digit_1 = first_number % 100
last_digit_2 = second_number % 100

print('Последние две цифры первого числа:', last_digit_1)
print('Последние две цифры второго числа:', last_digit_2)

summ = last_digit_1 + last_digit_2
print('Сумма этих чисел:', summ)