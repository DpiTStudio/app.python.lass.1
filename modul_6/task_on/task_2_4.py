client_name = input("Представьтесь уважаемый клиент? ")
client_credits = int(input("Сумма вашей за должности: "))
cash_in = 0
print("Уважаемый клиент: ", client_name, "\n",
      "Довожу до Вашего сведения, что у Вас образовалась за должность в размере: ", client_credits, sep="")
while cash_in < client_credits:
    cash_in = int(input("Сколько рублей вы внесете прямо сейчас, чтобы ее погасить? "))
    money = client_credits - cash_in
    if money < client_credits:
        print(client_name, money, "- ваш долг")
        if money > client_credits:
            cash_in = int(input("Добавьте еще для завершения: "))
print("Отлично,", client_name, "! Вы погасили долг. Спасибо!")