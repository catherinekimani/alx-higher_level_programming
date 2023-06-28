#!/usr/bin/python3
class Square:
    """
    This class represents a square

    Attributes:
            __size: private size of the square
    """
    def __init__(self, size=0):
        """
        Initializes a square object with an optional size

        Parameters:
                size: size of the square. 0
        Raises:
            TypeError: if size is not an integer
            ValueError: if size if < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
