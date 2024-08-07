print('Задача 8. Игра «Компьютер угадывает число»')
start = 1
finish = 101
count = 1

while True:
    n = (start + finish) // 2
    print('Твоё число равно, меньше или больше, чем число: ', n)
    answer = int(input('1 — равно, 2 — больше, 3 — меньше '))
    if answer == 1:
        print('Computer win)')
        break
    elif answer == 2:
        start = n
    elif answer == 3:
        finish = n
    count += 1

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче.
# Разбор подобного решения будет в следующем модуле.