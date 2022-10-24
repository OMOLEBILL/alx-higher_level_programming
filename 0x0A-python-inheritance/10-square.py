#!/usr/bin/python3
"""documentation for import
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)
