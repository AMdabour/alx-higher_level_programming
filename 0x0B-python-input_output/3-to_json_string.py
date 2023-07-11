#!/usr/bin/python3
"""define a function to convert a python obj into json data"""
import json


def to_json_string(my_obj):
    """convert my_obj into json data"""
    json_data = json.dumps(my_obj)
    return json_data
