"""
Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *)
with appropriate checking and error handling

```
class Fraction:
    pass

x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)
```
"""

from fraction import Fraction

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
