#!/usr/bin/python3
"""checks wether a classs is inherited
"""


def inherits_from(obj, a_class):
    """checks the inheritance of a class
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
