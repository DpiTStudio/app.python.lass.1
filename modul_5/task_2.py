money = 100
cheese_price = 60
ice_cream_price = 20

if money >= cheese_price:
    print("На сыр денег хватило")
    money -= cheese_price
    if money >= ice_cream_price:
        print("И на мороженое тоже!")
        money -= ice_cream_price
    else:
        print("Денег маловато")
else:
    print("Денег не хватило даже на сыр!")

# Маша пошла за сыром
# Мама дала Маше денег и отправила её в магазин за сыром. А ещё сказала: «Если останутся деньги, то можешь купить себе мороженое. Если денег на сыр не хватит, то денег маловато — а значит, и мороженого не будет».
# Сыр стоит 60 рублей, мороженое — 20 рублей.

# Сделайте программу, которая. 
# 1) считывает из переменной money количество полученных денег.
# 2) Если денег на сыр хватает (больше либо равно), то:
# 2.1) Выводите сообщение: «На сыр денег хватило». 
# 2.2) Вычитайте стоимость сыра из кошелька.
# 2.3) Если оставшихся денег хватает на мороженое,
# 2.3.1) то выводите: «И на мороженое тоже!»
# 2.3.2) Иначе выводите: «Денег маловато».
# 3) Если денег не хватило даже на сыр, то выводите: «Денег не хватило даже на сыр!»