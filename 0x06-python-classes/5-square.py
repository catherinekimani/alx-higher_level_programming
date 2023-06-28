#!/usr/bin/python3

class Square:
    """
    This class represents a square

    Attributes:
            __size: private size of the square
    """

    def __init__(self, size):
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
        Calculates and returns the current area of the square

        Returns:
            int: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout using "#"
        """
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()
