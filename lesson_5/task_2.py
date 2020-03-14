"""
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, 
and make a third list containing the common integers 
between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""

import random

list_1 = []
list_2 = []
while len(list_1) < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))

list_3 = []
index = 0
while index < len(list_1):
    if list_1[index] in list_2:
        list_3.append(list_1[index])
    index += 1

print(list(set(list_3)))
