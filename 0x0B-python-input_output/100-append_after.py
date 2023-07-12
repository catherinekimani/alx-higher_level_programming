#!/usr/bin/python3

""" Define function that inserts a new line of a text"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a new line after each line containing a specific string
    """
    txt = ""
    with open(filename) as a_file:
        for line in a_file:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w")as my_file:
        my_file.write(txt)
