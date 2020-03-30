"""
Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):

def __init__(self, msg):
...

"""

from custom_exception import CustomException

if __name__ == "__main__":
    raise CustomException("I'm error")
