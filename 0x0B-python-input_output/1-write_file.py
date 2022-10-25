#!/usr/bin/python3
"""creating a file and reading the number of characters
"""


def write_file(filename="", text=""):
    """writes and return the no of characters
    """
    with open(filename, "w+",  encoding='utf-8') as f:
        return f.write(text)
