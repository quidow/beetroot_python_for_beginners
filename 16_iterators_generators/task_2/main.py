"""
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
"""

if __name__ == "__main__":
    from in_range import in_range
    print(list(in_range(0, 10, 2)))
    print(list(in_range(10, 0, -2)))
