client_name = input("Представьтесь уважаемый клиент? ")
client_credits = int(input("Сумма вашей за должности: "))
cash = 0
print("Уважаемый клиент: ", client_name, "\n",
      "Довожу до Вашего сведения, что у Вас образовалась за должность в размере: ", client_credits, sep="")
while cash <= client_credits:
    cash = int(input("Сколько рублей вы внесете прямо сейчас, чтобы ее погасить? "))
    money = client_credits - cash
    if money == client_credits:
        print("Маловато ", client_name, ". Давайте ещё раз.", "\n",
              "Ваш долг на данный момент: ", money, sep="")
        cash = int(input("Сколько рублей вы внесете прямо сейчас, чтобы ее погасить? "))
print("Отлично,", client_name, "! Вы погасили долг. Спасибо!")