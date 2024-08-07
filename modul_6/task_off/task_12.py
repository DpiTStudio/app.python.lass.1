virus_inform = "Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!"
virus_inform_true = "Все верно скейт ты вернул! ПК разблокирован!"
virus_inform_input = "Введите пожалуйста пароль для получения доступа к ПК: "
virus_inform_pass_off = "Пароль не верен и твой ПК не будет разблокирован."
virus_pass = 1984

print(virus_inform)
while virus_pass != False:
    virus_pass_input = int(input(virus_inform_input))
    if virus_pass_input == virus_pass:
        print(virus_inform_true)
        break
    else:
        print(virus_inform_pass_off)