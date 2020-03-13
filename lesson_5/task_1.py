"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 
and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""

import random

random_num = random.randrange(1, 10)
promted_num = input("guess number: ")
if promted_num.isdigit():
    if random_num == int(promted_num):
        print("yep")
    else:
        print("nope, it was " + str(random_num))
else:
    print("your input is not number")
