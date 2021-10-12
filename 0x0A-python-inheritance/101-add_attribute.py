#!/usr/bin/python3

"""
add attribute if possible
or raise TypeError
"""


def add_attribute(obj, attribute, value):
    """
    check if obj is instance of non built in class
    """
    if not obj.__class__.__module__ == 'builtins':
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
