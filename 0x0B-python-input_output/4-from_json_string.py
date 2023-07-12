#!/usr/bin/python3

""" Define a func that returns an object """
import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string """
    obj_r = json.loads(my_str)
    return obj_r
