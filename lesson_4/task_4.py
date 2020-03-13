"""
The math quiz program

Write a program that asks the answer for a mathematical expression, 
checks whether the user is right or wrong, 
and then responds with a message accordingly.
"""

import random
import operator

num1 = random.randrange(1, 10)
num2 = random.randrange(1, 10)

ops = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv
    }

op = random.choice(list(ops.keys()))
result = ops.get(op)(num1,num2)

print("enter the right answer:")
answer = input(f'{num1} {op} {num2} = ')

try:
    if result == int(answer):
        print("you are right!")
    else:
        print("you are wrong!")
except:
    print("you entered not integer!")
