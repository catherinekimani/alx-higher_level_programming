#!/usr/bin/python3

""" Define a class Rectangle the inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.
        Args:
            width (int): width of the rect
            height (int): height of the rect
            x (int): cordinate of the rect's position
            y (int): cordinate of the rect's position
            id (int): id value
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get the width of the rect """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rect """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rect """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rect """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x coordinate of the rect's position """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x coordinate of the rect's position """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y coordinate of the rect's position """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y coordinate of the rect's position """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """ Display the rectangle using '#' character """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")
