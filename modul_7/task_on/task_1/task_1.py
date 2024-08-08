number = int(input('Введите число: '))
isPrime = True
for divider in range(2, number):
    if number % divider == 0:
        isPrime = False
        break
    if isPrime:
        print('Число простое')
    else:
        print('Число составное')