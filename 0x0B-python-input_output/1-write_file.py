#!/usr/bin/python3

""" Define a function that writes a string """


def write_file(filename="", text=""):
    """
    Writes to a text file
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
