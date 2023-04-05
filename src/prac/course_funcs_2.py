import pytest
import sys


def fizz(num):
    """return fizz if num is cleanly divisible by 3

    Args:
        num (int): an integer.
    """
    if num % 3 == 0:
        return "fizz"
    else:
        return num


def buzz(num):
    """return buzz if num is cleanly divisible by 5

    Args:
        num (int): an integer
    """
    if num % 5 == 0:
        return "buzz"
    else:
        return num
