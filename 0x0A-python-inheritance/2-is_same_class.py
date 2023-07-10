#!/usr/bin/python3

""" Define a function to check instance """


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class
    Args:
        obj: the object
        a_class: class to compare
    """
    return isinstance(obj, a_class) and type(obj) is a_class
