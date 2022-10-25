#!/usr/bin/python3
"""writing the json format into a txt
"""


import json
"""the json module
"""


def save_to_json_file(my_obj, filename):
    """save in json format
    """
    with open(filename, "w",  encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
