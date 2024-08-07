num = int(input("Введите число: "))
summa = 0
while num > 0:
    print("Последняя цифра: ", num % 10)
    if num % 10 == 5:
        break
    summa += num % 10
print(summa)
