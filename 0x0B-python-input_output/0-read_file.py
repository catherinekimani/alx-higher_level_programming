#!/usr/bin/python3

""" Define a function that reads a text file """


def read_file(filename=""):
    """
    Reads a text file & prints to stdout
    Args:
        filename (str): name if file to be read
    """
    with open(filename, encoding='utf-8') as a_file:
        read_f = a_file.read()
        print(read_f, end="")
