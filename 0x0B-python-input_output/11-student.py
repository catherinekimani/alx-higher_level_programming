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

    def to_json(self, attrs=None):
        """
        Dictionary representation of a student """
        if (type(attrs) == list and all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes of the student """
        for key, value in json.items():
            setattr(self, key, value)
