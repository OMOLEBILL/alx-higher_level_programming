#!/usr/bin/python3
"""This module uses the request package to give a specific variable"""


if __name__ == "__main__":
    import requests
    import sys

    data = requests.get(sys.argv[1])
    if data.status_code == 200:
        print(data.headers["X-Request-Id"])
