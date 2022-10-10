#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if str(value).isdigit():
            print("{:d}".format(value))
            return True
        else:
            return False
        except ValueError:
            print("no such thing")
