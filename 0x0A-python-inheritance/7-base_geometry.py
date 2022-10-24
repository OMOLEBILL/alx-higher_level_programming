#!/usr/bin/python3
"""Raises an exception
"""


class BaseGeometry():
    """ Raises ana exception
    """
    def area(self):
        """raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a values
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
