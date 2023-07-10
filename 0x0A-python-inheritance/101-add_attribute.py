#!/usr/bin/python3
""" Define function to add attribute to an object """


def add_attribute(obj, attr_name, attr_val):
    """
    Add attribute to an object

    Args:
        attr_name: attribute name
        attr_val: attribute value

    Raises:
        TYpeError: if a new attribute cannot be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_val)
