#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    z = max(a_dictionary.values())
    for keys in a_dictionary.keys():
            if a_dictionary[keys] == z:
                b = keys
     return b
