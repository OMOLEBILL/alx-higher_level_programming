#!/usr/bin/python3
"""This module handles error if they occur"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
