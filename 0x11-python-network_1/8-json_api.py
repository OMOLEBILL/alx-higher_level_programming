#!/usr/bin/python3
"""This module uses the request package to give a specific variable"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"

    q = argv[1] if len(argv) == 2 else ""
    data = requests.post(url, json={"q": q})
    try:
        cont = data.json()
        id, name = cont.get('id'), cont.get('name')
        if len(cont) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(cont.get("id"), cont.get("name")))
    except ValueError:
        print("Not a valid JSON")
