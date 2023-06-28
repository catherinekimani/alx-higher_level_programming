#!/usr/bin/python3
"""Defination of a class Square"""


class Square:
    """
    This class represents a square.

    Attributes:
            __size: Size of the square(private)
    """
    def __init__(self, size):
        """
        Initializes a square object with given size

        Parameters:
                size: size of the square
        """
        self.__size = size
