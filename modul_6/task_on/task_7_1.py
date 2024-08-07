print("Загадайте число от 1 до 100 (включительно)")

min_num = 1
max_num = 100
tries = 0

while True:
guess = random.randint(min_num, max_num)
answer = int(input(f"Твое число равно, меньше или больше чем число {guess}? (1 - равно, 2 - больше, 3 - меньше) "))
tries += 1

if answer == 1:
print(f"Компьютер угадал число за {tries} попыток!")
break
elif answer == 2:
min_num = guess + 1
elif answer == 3:
max_num = guess - 1

if tries == 7:
print("Компьютер не смог угадать число за 7 попыток")
break