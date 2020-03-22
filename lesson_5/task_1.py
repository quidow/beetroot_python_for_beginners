"""
The greatest number

Write a Python program to get the largest number from
a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""

import random

random_nums = []
while len(random_nums) < 10:
    random_nums.append(random.randint(0, 100))

print(max(random_nums))

