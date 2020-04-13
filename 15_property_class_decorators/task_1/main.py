"""
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter
is a valid email string.
"""

from class_decor import User

if __name__ == "__main__":
    user = User("username", "username@mail.com")
