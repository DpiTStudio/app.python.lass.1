wake_up = int(input("Когда вы проснулись? "))
awake_hours = 0
calories_sum = 0
for hour in range(wake_up, 24):
    print("Сейчас", hour, "часов")
    calories = int(input("Сколько сел за час? "))
    calories_sum += calories
    if calories_sum > 2000:
        print("Вам нужно отдохнуть.")
        break
    awake_hours += 1
print("Вы проснулись", awake_hours, "часов.")
print("Вы потратили", calories_sum, "ккал.")