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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
