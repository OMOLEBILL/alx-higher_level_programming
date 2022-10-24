#!/usr/bin/python3
"""class my list
"""


class MyList(list):
    """we inherit a classs list
    """
    def __init__(self):
        """inheritance
        """
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list
        """
        print(sorted(self))
