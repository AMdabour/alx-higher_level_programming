#!/usr/bin/python3

"""
define a module
"""


def is_same_class(obj, a_class):
    """returns True if obj is instance of a_class else False"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
