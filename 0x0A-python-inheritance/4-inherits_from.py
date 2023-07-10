#!/usr/bin/python3

""" Define a function to check instance """


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: the object
        class: class to compare
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
