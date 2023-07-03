#!/usr/bin/python3
""" Define a Rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0
    """
    Public class attribute to keep track of the no. of instances
    """

    print_symbol = '#'
    """
    Public class attribute to store symbol used for for string representation
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance

        Args:
            width: width of the rectangle (0)
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width of the Rectangle
        Returns:
                width of the rectangle
        """
        self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle
        Args:
            value: width value to set
        Raises:
                TypeError: if width is not an int
                ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the Rectangle
        Returns:
                height of the rectangle
        """
        self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle
        Args:
            value: height value to set
        Raises:
                TypeError: if height is not an int
                ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate the area of rectangle
        Returns:
                Area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the biger one based on the area
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: if rect_1, rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new rectangle instance with equal W and H
        Args:
            size: size of the square(0)
        """
        return cls(size, size)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec_st = []
        for _ in range(self.__height):
            [rec_st.append(str(self.print_symbol))for _ in range(self.__width)]
            if _ != self.__height - 1:
                rec_st.append("\n")
        return ("".join(rec_st))

    def __repr__(self):
        """
        Returns a string representation of a rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a given message when an instance of a
        Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
