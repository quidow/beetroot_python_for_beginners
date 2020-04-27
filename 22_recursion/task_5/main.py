# def sum_of_digits(digit_string: str) -> int:
#     """
#     >>> sum_of_digits('26') == 8
#     True
#
#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")
#     """

from sum_of_digits import sum_of_digits

if __name__ == "__main__":
    assert sum_of_digits('26') == 8
    sum_of_digits('test')
