#!/usr/bin/python3

"""define a module my_list"""


class MyList(list):
    """represents a class MyList"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
