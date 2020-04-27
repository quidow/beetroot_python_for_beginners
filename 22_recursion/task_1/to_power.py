from typing import Optional, Union


def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp > 1:
        return x * to_power(x, exp - 1)
    if exp == 1:
        return x
    if exp <= 0:
        raise ValueError("This function works only with exp > 0.")
