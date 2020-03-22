"""
Extracting numbers.

Make a list that contains all integers from 1 to 100,
then find all integers from the list that are divisible by 7
but not a multiple of 5, and store them in a separate list.
Finally, print the list.

Constraint: use only while loop for iteration
"""

list_1 = list(range(1, 101))
list_2 = []

index = 0
while index < len(list_1):
    if list_1[index] % 7 == 0 and list_1[index] % 5 != 0:
        list_2.append(list_1[index])
    index += 1

print(list_2)

