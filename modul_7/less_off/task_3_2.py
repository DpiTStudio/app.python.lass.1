begin_number = int(input('Введите начальное число (старт) ...'))
end_number = int(input('Введите конечное число (конец) ...'))
for number in range(begin_number, end_number + 1):
    print(number ** 2)