#!/usr/bin/python3

"""
define a module
"""


def inherits_from(obj, a_class):
    """
    returns True if obj is instance of a class that
    inherited from a_class else False
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
