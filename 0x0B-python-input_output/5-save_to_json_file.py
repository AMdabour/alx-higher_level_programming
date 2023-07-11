#!/usr/bin/python3
"""
define a function writes an obj to a text file using
json representation
"""
import json



def save_to_json_file(my_obj, filename):
    """writes json string to a file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
