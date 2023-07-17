#!/usr/bin/python3

""" Define a class name Base """


class Base:
    """ Base class for managing id attr in all future classes. """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for base
        Args:
            id (int): id value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
