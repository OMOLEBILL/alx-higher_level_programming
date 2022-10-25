#!/usr/bin/python3
"""load and saves arguement as a list
"""


import json
import sys
"""the sys module
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    arg_list = load_from_json_file(filename)
except FileNotFoundError:
    arg_list = []
finally:
    for i in sys.argv[1:]:
        arg_list.append(str(i))
    save_to_json_file(arg_list, filename)
