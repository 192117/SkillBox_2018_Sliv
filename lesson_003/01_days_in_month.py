# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# user_input = input("Введите, пожалуйста, номер месяца: ")
for user_input in range(15):
    month = int(user_input)
    print('Вы ввели', month)
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    if month in months_with_31_days:
        print('Кол-во дней: 31')
    elif month == 2:
        print('Кол-во дней: 28')
    elif month > 0 and month <= 12:
        print('Кол-во дней: 30')
    else:
        print('Номер месяца некорректный')
