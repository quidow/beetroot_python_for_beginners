"""
The birthday greeting program.

Write a program that takes your name as input,
and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
"""

name = input("enter your name: ")
age = input("enter your age: ")
if age.isdigit():
    age = int(age)
else:
    print("you entered invalid age")
    exit()

print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")

