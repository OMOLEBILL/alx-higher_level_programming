#!/usr/bin/python3
"""from json to file
"""


import json
"""the json module
"""


def load_from_json_file(filename):
    """from json to file
    """
    with open(filename, 'r') as f:
        return json.load(f)
