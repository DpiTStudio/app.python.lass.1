password = int(input("Введите пароль: "))
while password != 1234:
    print("Пароль неверный")
    password = int(input("Введите пароль: "))
print("Пароль верный")