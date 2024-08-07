weather = int(input("Сколько градусов на улице? "))
meters = 0
while weather > 15:
    meters += 20 # Чуть пробежали вперед
    weather -= 2 # Похолодало
    if weather <= 15:
        break
    meters += 10 # Прошли немного пешком
print("Пройдено метов: ", meters)