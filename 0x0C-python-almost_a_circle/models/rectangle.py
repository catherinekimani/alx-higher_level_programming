#!/usr/bin/python3
from models.base import Base
""" Define a class Rectangle the inherits from Base """


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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ Get the width of the rect """
            return self.__width

        @width.setter
        def width(self, value):
            """ Set the width of the rect """
            self.__width = value

        @property
        def height(self):
            """ Get the height of the rect """
            return self.__height

        @height.setter
        def height(self, value):
            """ Set the height of the rect """
            self.__height = value

        @property
        def x(self):
            """ Get the x coordinate of the rect's position """
            return self.__x

        @x.setter
        def x(self, value):
            """ set the x coordinate of the rect's position """
            self.__x = value

        @property
        def y(self):
            """ Get the y coordinate of the rect's position """
            return self.__y

        @y.setter
        def y(self, value):
            """ set the y coordinate of the rect's position """
            self.__y = value
