# Задача 2. Сумма чисел
# Напишите программу, где пользователь вводит любые два целых положительных числа. А программа суммирует все числа в диапазоне от первого до второго. Гарантируется, что первое введённое число всегда меньше второго.
# Пример:
# Введите первое число: 5
# Введите второе число: 10
# Сумма чисел от 5 до 10 равна 45

print('Задача 2. Сумма чисел')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

sum = 0
for i in range(first_number, second_number + 1):
    sum += i
print(f'Сумма чисел от {first_number} до {second_number} равна {sum}')  