#!/usr/bin/python3
"""define a function returning dict representation"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure"""
    return obj.__dict__
