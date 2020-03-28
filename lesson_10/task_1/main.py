"""
A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
"""

from person import Person

if __name__ == "__main__":
    person = Person(input("Enter first name: "), input("Enter last name: "), input("Enter age: "))
    person.talk()
