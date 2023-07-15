#!/usr/bin/python3
"""define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """reoresents rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize every new instance with width,
        height, x, y and id attributes
        """
        super().__init__(id)

        self.__width = width

        def get_width(self):
            """width getter method"""
            return self.__width

        def set_width(self, value):
            """width setter method"""
            self.__width = value

        self.__height = height

        def height_getter(self):
            """height getter method"""
            return self.__height

        def height_setter(self, value):
            """height setter method"""
            self.__height = value

        self.__x = x

        def x_getter(self):
            """x getter method"""
            return self.__x

        def x_setter(self, value):
            """x setter method"""
            self.__x = value

        self.__y = y

        def y_getter(self):
            """y getter method"""
            return self.__y

        def y_setter(self, value):
            """y setter method"""
            self.__y = value
