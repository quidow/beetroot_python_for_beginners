"""
Сделайте (руками) текстовый файл вида

Василий;vasya;pas!231
Ольга;olya;o44@12

Напишите консольную утилиту которая требует логин пароль и приветствует 
пользователя (по имени а не логину) если он ввел верно. 

сделайте возможность регистрации пользователя если утилита запущена с 
дополнительным параметром. 
предполагается что строки вы прочитаете в структуру и сделаете массив структур 
а потом по массиву проходите в поисках логина и пароля. 
"""

import argparse

parser = argparse.ArgumentParser(description='Demo application')
parser.add_argument('-r', action='store_true', help="""Path to JSON file 
                    to store phonebook entries""")
args = parser.parse_args()

f_name = "advanced_task_2_file"

users = []
with open(f_name, "r") as f:
    for line in f.readlines():
        line = line.rstrip().split(";")
        user = {}
        user["name"] = line[0]
        user["login"] = line[1]
        user["password"] = line[2]
        users.append(user)
    f.close

if args.r:
    user = []
    user.append(input("Enter your name:"))
    user.append(input("Enter your login:"))
    user.append(input("Enter your password:"))
    with open(f_name, "a") as f:
        f.write(";".join(user))
    print("You was successfully registered")
else:
    login = input("Login: ")
    password = input("Password: ")
    for user in users:
        if user["login"] == login and user["password"] == password:
            print("Hello, " + user["name"] + "!")
            break
    else:
        print("The specified user was not found")
