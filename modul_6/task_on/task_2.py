print('Задача 2. Коллекторы')
# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

client_name = input('Введите ваше имя: ')
amount_of_debt = int(input('Введите сумму вашего долга: '))
print(client_name,', ваша задолженность составляет', amount_of_debt, 'рублей.')
while amount_of_debt > 0:
    amount_of_payment = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    if amount_of_payment >= amount_of_debt:
        print('Отлично,', client_name, 'Вы погасили долг. Спасибо!')
        amount_of_debt = 0
    else:
        amount_of_debt -= amount_of_payment
print('Спасибо за погашение долга!')


