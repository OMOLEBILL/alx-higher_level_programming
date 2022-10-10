#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for i in my_list:
            if i <= x:
                print(i, end="")
                index += 1
        print()
    except IndexError:
        print()
    return index
