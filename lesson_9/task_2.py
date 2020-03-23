"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises
an exception if the two values given by the input function were not numbers, and if value b was zero
(cannot divide by zero).
"""


def test(a, b):
    try:
        a, b = int(a), int(b)
        if b == 0:
            raise ZeroDivisionError
    except ValueError:
        print("Given values are not numbers!")
    except ZeroDivisionError:
        print("Second number is zero!")
    else:
        return a ** 2 / b


print(test(input("Enter first number: "), input("Enter second number: ")))

