#!/usr/bin/python3
"""class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square that inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """module string represation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
