#!/usr/bin/python3
class MyInt(int):
    """class MyInt
    """
    def __init__(self, value):
        """initilaizes value
        """
        self.name = value

    def __eq__(self, other):
        """eq
        """
        return self.num != other

    def __ne__(self, other):
        """ne
        """
        return self.num == other
