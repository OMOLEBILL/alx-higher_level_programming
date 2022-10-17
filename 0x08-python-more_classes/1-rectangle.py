#!/usr/bin/python3
""" defines an empty rectaangle
"""


class Rectangle():
    """Empty class
    """
    def __init__(self, width=0, height=0):
        """Initililizes the class
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ return the value of size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
