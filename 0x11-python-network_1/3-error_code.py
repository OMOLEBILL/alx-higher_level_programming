#!/usr/bin/python3
"""This module handles error if they occur"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    url = argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
