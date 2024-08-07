bags = int(input("Сколько нужно перетащить мешков? "))
totalwaight = 0
bags_count = 0
while bags_count < bags:
    waight = int(input("Сколько весит мешок? "))
    totalwaight += waight
    bags_count += 1
    print("Перенесли мешков:", bags_count, "из", bags)
print("Общий вес мешков: ", totalwaight)