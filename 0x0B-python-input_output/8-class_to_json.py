#!/usr/bin/python3
"""define a function to convert class into json representation"""


def class_to_json(obj):
    """converts class into json format"""
    if isinstance(obj, MyClass):
        return {'name': obj.name, 'number': obj.number}
    return obj
