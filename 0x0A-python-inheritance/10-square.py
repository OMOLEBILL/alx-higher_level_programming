#!/usr/bin/python3
"""documentation for import
"""


Rectangle = __import__('9-rectangle').Rectangle


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

    def area(self):
        return self.__size * self__size
