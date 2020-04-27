# from typing import Optional
# def mult(a: int, n: int) -> int:
#     """
#     This function works only with positive integers
#
#     >>> mult(2, 4) == 8
#     True
#
#     >>> mult(2, 0) == 0
#     True
#
#     >>> mult(2, -4)
#     ValueError("This function works only with postive integers")
#     """

from mult import mult

if __name__ == "__main__":
    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
    mult(2, -4)
