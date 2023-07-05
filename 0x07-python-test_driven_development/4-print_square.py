#!/usr/bin/python3
# 4-print_square.py
""" Defines a function that prints a square with a given character"""


def print_square(size):
    """
    Prints a square of a given size using '#'
    Args:
        size: length of the square
    Raises:
            TypeError: if size is not an integer
            ValuError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        [print("#", end="") for _ in range(size)]
        print("")
