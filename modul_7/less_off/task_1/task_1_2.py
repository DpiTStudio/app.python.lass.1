winners = 0
for ticket in 345, 19, 67, 1020, 421:
    if ticket % 5 == 0:
        print(ticket, "Cчастливый билет")
        winners += 1
print("Кол-во победителей: ", winners)
# 345 19 67 1020 421