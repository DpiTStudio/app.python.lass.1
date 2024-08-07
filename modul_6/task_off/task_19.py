begs = int(input("Сколько нужно перетащить мешков? "))
totalwaight = 0
bags_coutn = 0
while bags_coutn < begs:
    waight = int(input("Сколько весит мешок? "))
    totalwaight += waight
    bags_coutn += 1
    print("Перенесли мешков:", bags_coutn, "из", begs)
print("Общий вес мешков: ", totalwaight)