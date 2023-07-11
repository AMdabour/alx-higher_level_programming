#!/usr/bin/python3
"""define a function to create an obj from jsonfile"""
import json


def load_from_json_file(filename):
    """create obj from jsonfile"""
    with open(filename) as f:
        obj = json.load(f)
        return obj
