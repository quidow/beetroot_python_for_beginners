def mult(a: int, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return a
    elif n > 1:
        return a + mult(a, n - 1)
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
