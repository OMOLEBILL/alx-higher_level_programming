#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    y = {}
    for keys, values in a_dictionary.items():
        y[keys] = values*2
    return y
