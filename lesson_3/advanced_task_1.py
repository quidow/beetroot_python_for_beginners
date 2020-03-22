"""
Получение от пользователя его номера телефона.
Программа в цикле пока не получит валидный номер запрашивает у пользователя
телефон и проверяет что это

1. +3
2. Один из наших операторов 066 050 067 063 (может еще какие)
3. проверки какие придумаете чтоб убедиться что вам не "подсунули" мусор.
"""

operator_codes = ["093", "063", "050", "066", "067"]
while True:
    phonenumber = input("Please, enter your phonenumber: ")
    if (
            phonenumber[:2] == "+3"
            and phonenumber[3:6] in operator_codes
            and len(phonenumber) == 13
            and phonenumber[1:].isdigit()
    ):
        print("Your phonenumber is valid!")
        break
    else:
        print("Your phonenumber is invalid!")

