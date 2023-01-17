#!/usr/bin/python3
"""This module uses the request package to give a specific variable"""


if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    data = requests.post(argv[1], json={"q": q})
    try:
        cont = data.json()
        if not cont:
            print("No result")
        else:
            print("[{}] {}".format(cont["id"], cont["name"]))
    except ValueError:
        print("Not a valid JSON")
