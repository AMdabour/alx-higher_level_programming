"""
define a modeule containing a function
returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns a list of the available attributes and methods"""

    return dir(obj)
