totalMonths = int(input("Сколько месяцев будем копить?: "))
sum = 0
for month in range(totalMonths):
    print("В месяце", month)
    money = int(input("Сколько денег внесли?: "))
    sum += money
print("За", totalMonths, "месяцев вы накопили", sum, "рублей.")