#!/usr/bin/python3

"""BaseGeometry module with BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents Rectangle"""
    def __init__(self, width, height):
        """initilize new instance with width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
