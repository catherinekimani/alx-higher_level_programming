#!/usr/bin/python3

""" Define a class named Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Representation of a class Square
    """

    def __init__(self, size):
        """
        initialize a square
        Args:
            size: square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
