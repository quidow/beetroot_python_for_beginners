"""
программа играет с человеком угадывая загаданное число.
но не методом урезания промежутка пополам,
а выбирая рандомное число из промежутка.
"""

import random

num_min = 1
num_max = 100

print("guess the number in the range from 1 to 100")
print("write 'y' if I guessed right")
print("write 'b' if your number is bigger")
print("write 'l' if your number is lesser")
while True:
    if num_min > num_max:
        print("your number is not between 1 and 100")
        exit()
    else:
        num_random = random.randint(num_min, num_max)
        x = input("is " + str(num_random) + " your number? ")
        if x == "y":
            print("hurray!")
            exit()
        elif x == "b":
            num_min = num_random + 1
        elif x == "l":
            num_max = num_random - 1

