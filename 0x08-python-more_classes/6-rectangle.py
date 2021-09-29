#!/usr/bin/python3
"""Rectangle Class
A Rectangle Class
"""


class Rectangle:
    number_of_instances = 0
    """__init__

    The __init__ method initializes the size value of the Rectangle.

    Attributes:
        width (:obj:`int`, optional): The width of the Rectangle.
        height (:obj:`int`, optional): The height of the Rectangle.

    Raises:
        TypeError: If `size` type is not `int`.
        ValueError: If `size` is less than `0`.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += '\n'.join('#' * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
