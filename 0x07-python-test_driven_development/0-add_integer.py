#!/usr/bin/python3
# 0-add_integer.py
""" Defines a function that adds two integers"""


def add_integer(a, b=98):
    """
    Adds two integers & returns the result
    Args:
        a : integer or float to be added
        b : integer or float to be added(98)
    Raises:
            TypeError: If a or b is not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    res = a + b
    return int(res)
