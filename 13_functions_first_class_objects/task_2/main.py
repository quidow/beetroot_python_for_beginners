"""
Write a Python program to access a function inside a function
(Tips: use function, which returns another function)
"""

from exponentiation import exponentiation
from counter import counter

if __name__ == "__main__":
    exp2 = exponentiation(2)
    print(exp2(2))
    exp4 = exponentiation(4)
    print(exp4(2))

    count = counter()
    for i in range(3):
        print(count())
