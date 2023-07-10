#!/usr/bin/python3

""" Define a class named Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Representation of a class Rectangle that
    inherits BaseGeometry class
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle

        Args:
            width (int): width of the rect
            height (int): height of the rect
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate the rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of a rectangle
        """
        str_rect = "[" + str(self.__class__.__name__) + "] "
        str_rect += str(self.__width) + "/" + str(self.__height)
        return str_rect
