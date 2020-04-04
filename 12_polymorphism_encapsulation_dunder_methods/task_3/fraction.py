class Fraction:

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self):
        return f"Fraction({self.numerator}/{self.denominator})"

    def __repr__(self):
        return self.__str__()
