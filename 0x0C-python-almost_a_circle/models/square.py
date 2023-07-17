#!/usr/bin/python3

""" Define a class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):

        """
        Class constructor for square
        Args:
            size (int): size of the square
            x (int): x coordinate of the square's position
            y (int): y coordinate of the square's position
            id (int): id value
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Return string representation of a square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
