#!/usr/bin/python3
"""Raises an exception
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle, checks valididty
    """
    def __init__(self, width, height):
        """initiliazes the instance
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
