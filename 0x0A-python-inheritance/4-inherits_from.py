#!/usr/bin/python3
"""checks wether a classs is inherited
"""


def inherits_from(obj, a_class):
    """checks the inheritance of a class
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return False
    return True
