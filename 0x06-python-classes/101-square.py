#!/usr/bin/python3
"""Defination of a class Square."""


class Square:
    """
    This class represents a square

    Attributes:
            size(int): private size of the square
            position(tuple):position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the square class
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(idx, int) for idx in value) or
                not all(idx >= 0 for idx in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current area of the square

        Returns:
            int: Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square to stdout using "###"
        """
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print("")

    def __str__(self):
        """
        Prints representation of a square
        """
        if self.__size != 0:
            [print("") for _ in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="")for _ in range(0, self.__position[0])]
            [print("#", end="")for _ in range(0, self.__size)]
            if a != self.__size - 1:
                print("")
        return ("")
