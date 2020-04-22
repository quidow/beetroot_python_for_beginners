"""
Imports practice

Make a directory with 2 modules; make a function in one of them;
then import this function in the other module and use that in your script of choice.
"""

from module2 import hello

if __name__ == "__main__":
    print(hello())
