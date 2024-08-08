N = (100 + 1) // 2
while True:
    print("Твое число равно, больше или меньше числа", N, "?")
    answer = int(input("1 - равно, 2 - больше, 3 - меньше: "))
    if answer == 1:
        print("Компьютер угадал число")
        break
    elif answer == 2:
        N -= 1
    else:
        N += 1
    