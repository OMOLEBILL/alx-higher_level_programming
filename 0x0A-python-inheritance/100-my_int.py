#!/usr/bin/python3
""" module
"""


class MyInt(int):
    """class MyInt
    """
    def __eq__(self, other):
        """eq
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ne
        """
        return super().__eq__(other)
