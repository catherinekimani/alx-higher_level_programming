#!/usr/bin/python3

""" Define a function named lookup"""


def lookup(obj):
    """
    returns a list of available attributes & methods of an object
    Args:
        obj: the object
    """
    return dir(obj)
