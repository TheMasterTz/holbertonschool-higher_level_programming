#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """informal string representation of the rectangle"""
        return ("[Rectangle] {}/{}"
                .format(str(self.__width), str(self.__height)))

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
