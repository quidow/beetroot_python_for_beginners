"""
Write a Python program to detect the number of local variables declared in a function.
"""

from var_func import abc

if __name__ == "__main__":
    print(abc.__code__.co_nlocals)
