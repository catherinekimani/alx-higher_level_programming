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

    @property
    def size(self):
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return string representation of a square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update the attributes of the square """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int) and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dict representation of a square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
