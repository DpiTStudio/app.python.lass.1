print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге.
# Напишите программу, которая считала бы для него, сколько цифр во вводимом числе. Обратите внимание, что число 0 имеет одну цифру.
# Пример:
# Введите число: 567
# Ответ: 3
# Введите число: 1203
# Ответ: 4
counting_number_of_letters = int(input('Введите число: '))
number_of_digits = 0
while counting_number_of_letters > 0:
    number_of_digits += 1
    counting_number_of_letters = counting_number_of_letters // 10
print(number_of_digits)

# number = int(input('Введите число: '))
# decimal = 0
# while number > 0:
#   decimal += 1
#   number = number // 10
# print(decimal)