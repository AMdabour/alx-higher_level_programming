#!/usr/bin/python3

"""define a class Square"""


class Square:

    """represents a square"""

    def __init__(self, size=0):
        
        """
        initialize a new square

        Args:
        size(int): size of the new square
        """

        self._Square__size = size

        if type(self._Square__size) != int:
            raise TypeError("size must be an integer")
        elif self._Square__size < 0:
            raise ValueError("size must be >= 0")
