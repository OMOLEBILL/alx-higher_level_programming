#!/usr/bin/python3
""" prints a string
"""


def text_indentation(text):
    """prints a strings
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for m in ".:?":
        text = (m + "\n\n").join(
            [ln.strip(" ") for ln in text.split(m)])
    print("{}".format(text), end="")
