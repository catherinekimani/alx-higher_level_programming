#!/usr/bin/python3

"""
Define a func that returns the dict description
with simple data structure
"""


def class_to_json(obj):
    """ returns the dict description with simple data structure """
    return obj.__dict__
