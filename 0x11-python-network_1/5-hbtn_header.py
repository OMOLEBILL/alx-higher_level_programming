#!/usr/bin/python3
"""This module uses gets the value of a specific key"""


if __name__ == "__main__":
    import requests
    import sys


    data = requests.get(sys.argv[1])
    print(data.headers.get("X-Request-Id"))
