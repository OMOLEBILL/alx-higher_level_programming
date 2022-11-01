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

    @property
    def size(self):
        """ return the value of width
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square
        """
        if len(args):
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
