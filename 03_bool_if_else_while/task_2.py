"""
The valid phone number program.

Make a program that checks if a string is in the right format
for a phone number. The program should check that the string contains only
numerical characters and is only 10 characters long. Print a suitable message
depending on the outcome of the string evaluation.
"""

phonenumber = input("Please, enter your phonenumber: ")
if len(phonenumber) == 10 and phonenumber.isdigit():
    print("Your phonenumber is valid!")
else:
    print("Your phonenumber is invalid!")

