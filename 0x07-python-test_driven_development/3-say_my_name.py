#!/usr/bin/python3
# 3-say_my_name.py
""" Defines a function that prints a given string"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    Args:
        first_name: string representing first name
        last_name: string representing last name("")
    Raises:
            TypeError:
            if the first_name or last_name is not a string
    Returns:
            None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
