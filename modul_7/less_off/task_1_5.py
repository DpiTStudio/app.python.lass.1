# Задача 3. Лотерея 2
# Напишите программу для немного усложнённой версии задачи про выигрышные билеты. Есть заранее известные номера билетов: 345, 19, 87, 1020 и 421 (можете брать свои номера, не стесняйтесь). Теперь, билет считается выигрышным, если номер билета - трёхзначное число и оно делится на 5. Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.

print('Задача 3. Лотерея 2')
winners = 0
print("Можете брать свои номера, не стесняйтесь.")
for ticket in 345, 19, 87, 1020, 421:
    if ticket >= 100 and ticket <= 999:
        print(ticket, "победитель!")
        winners += 1
print("Кол-во победителей: ", winners)

