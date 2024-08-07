your_money = 100000

# Введите ваше решение ниже

if your_money < 0:
    print("Ошибка: доход не может быть отрицательным")
elif your_money < 10000:
    print("Налог равен:", your_money * 0.13)
elif your_money < 50000:
    print("Налог равен:", your_money * 0.2)
else:
    print("Налог равен:", your_money * 0.3)