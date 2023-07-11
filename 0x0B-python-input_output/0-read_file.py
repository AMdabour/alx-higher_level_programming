#!/usr/bin/python3
"""
defines a function for reading a file and printing its content
"""


def read_file(filename=""):
    """reads a file and prints it"""
    with open(filename, encoding="utf-8") as f:
        read_content = f.read()
        print(read_content)
