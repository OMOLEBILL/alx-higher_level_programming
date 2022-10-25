#!/usr/bin/python3
"""Reads froma file
"""


def read_file(filename=""):
    """reads froma a file
    """
    with open(filename, 'r',  encoding='utf-8') as f:
        print(f.read(), end="")
