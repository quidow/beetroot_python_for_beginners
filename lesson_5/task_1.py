"""
The greatest number

Write a Python program to get the largest number from 
a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""

import random

random_nums = []
for i in range(0, 10):
    random_nums.append(random.randint(0, 100))

max_num = 0
for n in random_nums:
    if n > max_num:
        max_num = n
print(max_num)
