#!/usr/bin/python3

"""
define a module
"""


def is_same_class(obj, a_class):
    """returns True if obj is exactly an instance of a_class else False"""

    return type(obj) is a_class
