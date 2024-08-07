print("Начался 8-часовой рабочий день")
hour = 0
time = 0
work = 0
homework = 0
while time != 8 :
    hour += 1
    print(hour, "час")
    time += 1
    tasks = int(input("Сколько задач решит Максим? "))
    work += tasks
    wife = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет) "))
    if wife == 1:
        homework += 1
        print("Рабочий день закончился. Всего выполнено задач: ", work)
    if homework > 0:
        print("Нужно зайти в магазин.")