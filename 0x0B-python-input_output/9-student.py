#!/usr/bin/python3

""" Define a class named Student """


class Student:
    """ Represents a Student """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new instance of Student class

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Dictionary representation of a student """
        return self.__dict__
