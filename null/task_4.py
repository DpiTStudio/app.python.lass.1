number = int(input("Введите число: "))
summ = 0
while number != 0:
    last_num = number % 10
    print(last_num)
    if last_num == 5:
        print("Обнаружен разрыв")
        break
    summ += last_num
    number //= 10
print("Сумма: ", summ)

# number // 10
# number % 10