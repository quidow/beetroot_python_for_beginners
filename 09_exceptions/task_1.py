"""
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""

import random


def oops():
    exceptions = (IndexError, KeyError)
    raise random.choice(exceptions)


def call_oops():
    try:
        oops()
    except IndexError:
        print("This is IndexError!")
    except KeyError:
        print("This is KeyError!")


call_oops()

