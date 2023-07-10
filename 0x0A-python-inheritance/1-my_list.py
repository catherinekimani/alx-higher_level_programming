#!/usr/bin/python3

""" Define a class that inherits from a List"""


class MyList(list):
    """
    A class that represents a list of ints
    """
    def print_sorted(self):
        """
        prints the list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
