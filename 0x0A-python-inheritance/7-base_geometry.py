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
        if type(name) != str:
            raise TypeError("name should be a string")
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
