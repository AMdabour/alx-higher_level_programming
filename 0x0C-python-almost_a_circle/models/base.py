#!/usr/bin/python3
"""define a base class"""


class Base():
    """represents a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize any new instance with id instance attribute"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
