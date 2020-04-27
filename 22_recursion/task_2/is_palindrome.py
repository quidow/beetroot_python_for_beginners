def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) < 2:
        return True
    if looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1], index)
    else:
        return False
