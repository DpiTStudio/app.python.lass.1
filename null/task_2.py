balance = int(input("Сколько денег пришло? "))
while balance > 5000:
    product_cost = int(input("Введите стоймость товара: "))
    balance -= product_cost
print("Внимание: на карте осталось мало денег.")
print("Баланс счета: ", balance)