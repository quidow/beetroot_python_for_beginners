"""
Нужен скрипт который будет искать в реестре физлиц информацию по ФОПу по ИНН и выводить на консольк структуру.
Ссылку на реестр прикладываю: https://data.gov.ua/dataset/1c7f3815-3259-45e0-bdf1-64dca07ddc10
"Єдиний державний реєстр юридичних осіб, фізичних осіб-підприємців та громадських формувань "

1. скачать архи и распаковаь
2. написать скрипт который принимает из строки запуска параметр и ищет данные о таком ФОПе.
"""

from ukraine_fop import find_fop

if __name__ == "__main__":
    file_path = '17.1-EX_XML_EDR_UO_FULL_10.04.2020.xml'
    user_choice = input('Enter 1 if you want to search by record number, or 2 by edrpou: ')
    if user_choice == '1':
        record = input('Enter record number: ')
        print(find_fop(file_path, record=record))
    if user_choice == '2':
        edrpou = input('Enter edrpou: ')
        print(find_fop(file_path, edrpou=edrpou))
