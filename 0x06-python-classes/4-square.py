#!/usr/bin/python3

"""
class Sqaure qith a private instance attribute siz
"""


class Square:
    """
    Class Square with a private instance attribute size
    """
    def __init__(self, size=0):
        """ args:
                 size
        """
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
    Returns area
    """

    def area(self):
        """
        Return the area of the sqaure
        """
        return (self.__size * self.__size)
