#!/usr/bin/python3
"""We get the base class from the modules base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """we initialize the the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width
        """
        return (self.__width)

    @width.setter
    def width(self, width):
        """ set the value of width
        """
        self.__width = width

    @property
    def height(self):
        """ return the value of height
        """
        return (self.__height)

    @height.setter
    def height(self, height):
        """ sets the value of height
        """
        self.__height = height

    @property
    def x(self):
        """ return the value of x
        """
        return (self.__x)

    @x.setter
    def x(self, x):
        """ sets the value of x
        """
        self.__x = x

    @property
    def y(self):
        """ returns the value of y
        """
        return (self.__y)

    @y.setter
    def y(self, y):
        """ sets the value for y
        """
        self.__y = y
