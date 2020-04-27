# from typing import Optional
# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
#     """
#     Returns  x ^ exp
#
#     >>> to_power(2, 3) == 8
#     True
#
#     >>> to_power(3.5, 2) == 12.25
#     True
#
#     >>> to_power(2, -1)
#     ValueError: This function works only with exp > 0.
#     """
#     pass

from to_power import to_power

if __name__ == "__main__":
    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25
    to_power(2, -1)
