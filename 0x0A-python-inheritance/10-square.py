#!/usr/bin/python3
"""documentation for import
"""


Rectangle = __import__('9-rectangle.py').Rectangle


"""class Square
"""


class Square(Rectangle):
    """class square
    """
    def __init__(self, size):
        """ initialize an instance
        """
        self.__size = size
        super().__init__(self.__size, self.__size)
