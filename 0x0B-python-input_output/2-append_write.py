#!/usr/bin/python3

""" function that appends a string """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a txt file
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
