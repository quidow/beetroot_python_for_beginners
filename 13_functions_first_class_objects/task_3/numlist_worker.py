def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    if not isinstance(nums, list):
        raise TypeError
    if not callable(func1):
        raise TypeError
    if not callable(func2):
        raise TypeError
    if all(i > 0 for i in nums):
        return func1(nums)
    else:
        return func2(nums)
