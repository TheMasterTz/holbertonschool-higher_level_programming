#!/usr/bin/python3
"""
    Checks if the `obj` is an instance of `a_class` that inherited (directly or indirectly)

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object
    Returns:
        `True` if the object is an instance or inherit from the
        specified class; otherwise `False`
"""


def inherits_from(obj, a_class):
    """function inherits_from"""
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
