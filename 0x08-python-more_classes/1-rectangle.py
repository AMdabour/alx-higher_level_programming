#!/usr/bin/python3

"""define a class named rectangle"""


class Rectangle:

    """represents a class"""

    def __init__(self, width=0, height=0):
        """initialize any created instance with width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """a method for retrieving width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter function"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a method for retrieving height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter function"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
