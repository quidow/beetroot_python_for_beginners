async def fibonacci(n):
    if n in (1, 2):
        return 1
    return await fibonacci(n - 1) + await fibonacci(n - 2)


async def factorial(n):
    if n == 1:
        return n
    else:
        return n * await factorial(n - 1)


async def square(n):
    return n ** 2


async def cube(n):
    return n ** 3
