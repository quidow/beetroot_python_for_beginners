"""
программа играет с человеком угадывая загаданное число. 
но не методом урезания промежутка пополам, 
а выбирая рандомное число из промежутка.
"""

import random

range_list = list(range(1, 101))

print("guess the number in the range from 1 to 100")
print("write 'y' if I guessed right")
print("write 'b' if your number is bigger")
print("write 'l' if your number is lesser")
while True:
    num_random = random.randint(range_list[0], range_list[-1])
    print(range_list)
    x = input("is " + str(num_random) + " your number? ")
    if x == "y":
        print("hurray!")
        exit()
    elif x == "b":
        index = range_list.index(num_random)
        range_list = range_list[index + 1:]
    elif x == "l":
        index = range_list.index(num_random)
        range_list = range_list[:index]
