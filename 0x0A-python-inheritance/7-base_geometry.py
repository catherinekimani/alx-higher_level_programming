#!/usr/bin/python3

""" Define a class named BaseGeometry """


class BaseGeometry:
    """ A base class """

    def area(self):
        """
        Public instance method to raise an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value
        Args:
            name (str): name of the value being validated
            value (int): value being validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
