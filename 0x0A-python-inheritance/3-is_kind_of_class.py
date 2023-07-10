#!/usr/bin/python3

""" Define a function to check instance """


def is_kind_of_class(obj, a_class):
    """
    Check if an object is  an instance or a given subclass
    Args:
        obj: the object
        a_class: class to compare
    """
    if isinstance(obj, a_class):
        return True
    return False
