#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listz = my_list[:]
    if 0 <= idx < len(my_list):
        listz[idx] = element
        return(listz)
    return(my_list)
