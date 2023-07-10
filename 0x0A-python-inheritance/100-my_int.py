#!/usr/bin/python3

""" Define a class named MyInt """


class MyInt(int):
    """
    A rebel class that inherits from int
    """
    def __eq__(self, value):
        """
        Overrides the equality operator (==)
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
        Overrides the inequality operator (!=)
        """
        return super().__eq__(value)
