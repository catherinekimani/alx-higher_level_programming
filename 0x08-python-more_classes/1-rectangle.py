#!/usr/bin/python3
""" Defines a Rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance

        Args:
            width: width of the rectangle (0)
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width of the Rectangle
        Returns:
                width of the rectangle
        """
        self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle
        Args:
            value: width value to set
        Raises:
                TypeError: if width is not an int
                ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the Rectangle
        Returns:
                height of the rectangle
        """
        self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle
        Args:
            value: height value to set
        Raises:
                TypeError: if height is not an int
                ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
