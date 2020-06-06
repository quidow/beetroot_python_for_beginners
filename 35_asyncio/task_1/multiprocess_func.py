def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def square(n):
    return n ** 2


def cube(n):
    return n ** 3
