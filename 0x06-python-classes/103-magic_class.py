#!/usr/bin/python3

"""Definition of a class MagicClass"""

import math


class MagicClass:
    """Representation of a circle"""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass with a given radius.
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the MagicClass.
        """
        return 2 * math.pi * self.__radius
