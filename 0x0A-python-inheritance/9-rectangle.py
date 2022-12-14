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

    def area(self):
        """returns the area
        """
        return self.__width * self.__height

    def __str__(self):
        """prints string
        """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
