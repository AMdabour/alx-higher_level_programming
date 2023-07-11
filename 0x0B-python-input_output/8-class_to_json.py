#!/usr/bin/python3
"""define a function to convert class into json representation"""
import json


def class_encoder(obj):
    """encodes obj"""
    if isinstance(obj, MyClass):
        return {'name': obj.name, 'number': obj.number}
    return obj

def class_to_json(obj):
    """class to json"""
    jsonrepr = hson.dumps(obj, default=class_encoder)
    return jsonrepr
