# Задача 1. Надоедливый заказчик
# Нашему заказчику нужно, чтобы фраза «Я — программист!» выводилась на экран столько раз, сколько он сам этого захочет.
# Напишите программу, которая запрашивает число — количество строчек с фразой «Я — программист!» — и столько же раз выводит на экран эту фразу. Для решения задачи используйте переменную-счётчик, которая увеличивается на единицу до тех пор, пока не будет выведено нужное количество строчек.

# Переменные.
label = "Я — программист!"
numbers_label_1 = "По вашему требованию мы вывели"
numbers_label_2 = "строки"
text_label_input = "Количество повторов строки: "
number_list = 0
# Запрос с клиента.
numbers_lists = number = int(input(text_label_input))
# Просчет и вывод в цикле.
while number_list < number:
    print(label)
    number_list += 1
print(numbers_label_1, numbers_lists, numbers_label_2)
