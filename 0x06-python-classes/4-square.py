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
        self.size = size

    """
    reutns size
    """

    @property
    def size(self):
        """
        Returns the value of size
        """
        return (self.__size)

    """
    Size sets the values of size
    """

    @size.setter
    def size(self, size):
        """
        Raises an exception if the contions are not met
        args:
             size
        """
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
