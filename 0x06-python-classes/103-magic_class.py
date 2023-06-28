#!/usr/bin/python3

"""Defination of a class MagicClass"""


import math


class MagicClass:
    """Representation of a circle"""
    def __init__(self, radius=0):
        """
        Initialize a MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Area of MagicClass
        """
        return self.__radius ** 2 * math.pi

    def circumfrence(self):
        """
        Returns the circumfrence
        """
        return 2 * math.pi * self.__radius
