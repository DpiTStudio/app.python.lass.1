# Функция range()
for i in range(1, 10):
    if i % 4 == 0:
        print("Делимое найдено", i)
        break
    print(i, "Не делится без остатка! Продолжаю искать")
else:
    print("Ни одного делимого не было найдено")
# Эта функция позволяет быстро создать нужную последовательность чисел.
# Синтаксис
# range(<start>, <stop>) — start и stop здесь указывают на начало и конец последовательности, причём start по умолчанию равен 0, а stop не включает последнее число диапазона. То есть если мы напишем
# range(3), то получим последовательность 0, 1, 2 (от 0 до 3, не включая 3).
# range(10, 15) позволит нам начать не с 0, а с 10: 10, 11, 12, 13, 14.
# Конструкция for-else 
# Для работы с циклом for вы также можете использовать конструкцию for-else. Эта конструкция в Python позволяет выполнить блок кода, если цикл for завершился нормально. Это может быть полезно, если вы хотите выполнить какие-то действия после завершения цикла for.
# Вы также можете использовать оператор break для остановки цикла внутреннего вложения for. 
# Например, у вас есть диапазон чисел и вы хотите проверить, есть ли в нём число, делящееся на 3. В этом случае вы можете использовать цикл for для перебора элементов и оператор if для проверки каждого элемента. Если число найдено, можно использовать оператор break, чтобы прервать цикл. Если же число не найдено, то можно выполнить блок кода в конструкции else. 
# for i in range(1, 5):
#     if i % 3 == 0:
#         print("Делимое найдено", i)
#         break
#     print(i, "Не делится без остатка! Продолжаю искать")
# else:
#     print("Ни одного делимого не было найдено")