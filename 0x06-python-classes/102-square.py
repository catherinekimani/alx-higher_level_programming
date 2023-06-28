#!/usr/bin/python3
"""Defination of a class Square."""


class Square:
    """
    This class represents a square

    Attributes:
            __size: private size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a square object with given size

        Parameters:
                size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves size of the square

        Returns:
            int: size of the suare
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size of the square

        Parameters:
            value: size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size if < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            Area of current square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Compare if two squares have equal areas"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have unequal areas"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if one square has a greater area than the other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square has a greater or equal area than the other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if one square has a smaller area than the other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square has a smaller or equal area than the other"""
        return self.area() <= other.area()
