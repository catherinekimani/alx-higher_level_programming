#!/usr/bin/python3

""" Define a class Rectangle the inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.
        Args:
            width (int): width of the rect
            height (int): height of the rect
            x (int): cordinate of the rect's position
            y (int): cordinate of the rect's position
            id (int): id value
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get the width of the rect """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rect """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rect """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rect """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieve x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x coordinate of the rect's position """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieve y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y coordinate of the rect's position """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """ Display the rectangle using '#' character """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for a in range(self.__width + self.__x):
                if a < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """ Return string representation of the rect """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update the attributes of the rectangle """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int) and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return dict representation of a rectangle """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
