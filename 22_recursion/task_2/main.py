# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     """
#     Checks if input string is Palindrome
#     >>> is_palindrome('mom')
#     True
#
#     >>> is_palindrome('sassas')
#     True
#
#     >>> is_palindrome('o')
#     True
#     """
#     pass

from is_palindrome import is_palindrome

if __name__ == "__main__":
    assert is_palindrome('mom')
    assert is_palindrome('sassas')
    assert is_palindrome('o')
