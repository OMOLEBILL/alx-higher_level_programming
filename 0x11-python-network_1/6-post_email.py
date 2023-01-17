#!/usr/bin/python3
"""This module posts data"""


if __name__ == "__main__":
    import requests
    from sys import argv

    data = requests.post(argv[1], data={"email": argv[2]})
    print(data.text)
