def exponentiation(exponent):
    if not isinstance(exponent, int):
        raise TypeError

    def result(num):
        if not isinstance(num, int):
            raise TypeError
        return num ** exponent

    return result
