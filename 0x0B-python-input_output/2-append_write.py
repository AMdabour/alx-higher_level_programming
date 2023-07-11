#!/usr/bin/python3
"""
define a functions that appends a string to the end of a file
and returns the nb_written
"""


def append_write(filename="", text=""):
    """appends a string to  a file and returns nb_written"""
    with open(filename, 'a', encoding="utf-8") as f:
        nb_written = f.write(text)
        return nb_written
