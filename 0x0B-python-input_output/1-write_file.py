#!/usr/bin/python3
"""
define a function writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """write a string to a text file and returns nb_written"""
    with open(filename, 'w', encoding="utf-8") as f:
        nb_written = f.write(text)
        return nb_written
