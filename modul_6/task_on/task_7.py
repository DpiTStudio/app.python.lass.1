print('Задача 7. Игра «Угадай число»')
number = int(input('Введи число которое я загадал: '))
# Одна попытка уже использована
attempts = 1
# Загаданное число
while number != 7:
    # Плюс одна попытка за цикл
    attempts += 1
    if number > 7:
        print('Число больше, чем необходимо. Попробуй еще разок!')
        number = int(input('Введите число: '))
    elif number < 7:
        print('Число меньше, чем необходимо. Попробуй еще разок!')
    number = int(input('Введите число: '))
print('Вы угадали.', 'Количество попыток: ', attempts)

# В одной из практических работ мы делали задачу, где папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4