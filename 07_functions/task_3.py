"""
A simple calculator.
s
Create a function called make_operation,
which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter.

For example:

- the call make_operation(‘+’, 7, 7, 2) should return 16
- the call make_operation(‘-’, 5, 5, -10, -20) should return 30
- the call make_operation(‘*’, 7, 6) should return 42
"""

import operator


def make_operation(op, num=None, *args):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    result = num
    if args:
        for i in args:
            result = ops.get(op)(result, i)
    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))

