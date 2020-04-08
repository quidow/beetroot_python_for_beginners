"""
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:

"add called with 4, 5"

```
def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

```
"""

from func_decor import add, square_all

if __name__ == "__main__":
    add(2, y=2)
    square_all(2, 3, 4)
