# Задача 2. Расшифровка кода
#
# Нам нужно расшифровать определённый код в виде одного большого числа. Для этого нужно посчитать сумму цифр справа налево.
# Если мы встречаем в числе цифру 5, то выводим сообщение «Обнаружен разрыв» и заканчиваем считать сумму.
# В конце программы на экран выводится сумма тех цифр, которые мы взяли.
#
numbers = int(input("Введите число: "))
summ_of_numbers = 0
while numbers != 0:
    last_number = numbers % 10
    if last_number == 5:
        print("Обнаружен разрыв")
        break
    summ_of_numbers += last_number
    numbers //= 10

print(summ_of_numbers)