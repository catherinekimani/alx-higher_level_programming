#!/usr/bin/python3

""" Dfine function that returns JSON representation of an obj """
import json


def to_json_string(my_obj):
    """
    returns JSON Representation of an object
    args:
        my_obj: object to convert
    """
    return json.dumps(my_obj)
