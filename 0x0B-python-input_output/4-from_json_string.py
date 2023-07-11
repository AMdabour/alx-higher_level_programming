#!/usr/bin/python3
"""define a function to decode a json string"""
import json


def from_json_string(my_str):
    """decode my_str and convert it into python obj"""
    python_obj = json.loads(my_str)
    return python_obj
