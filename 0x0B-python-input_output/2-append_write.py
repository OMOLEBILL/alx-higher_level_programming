#!/usr/bin/python3
"""returning the number of appended characters to a file
"""


def append_write(filename="", text=""):
    """returning the o of appended charcters
    """
    with open(filename, "a",  encoding='utf-8') as f:
        return(f.write(text))
