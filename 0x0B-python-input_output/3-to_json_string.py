#!/usr/bin/python3
"""returns a json representation of an object
"""


import json
""" the json module
"""


def to_json_string(my_obj):
    """return a json rep of an object
    """
    return (json.dumps(my_obj))
