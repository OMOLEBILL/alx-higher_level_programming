#!/usr/bin/python3
"""This module uses the request package to get the body of a url"""


if __name__ == "__main__":
    import requests

    data = requests.get("https://alx-intranet.hbtn.io/status")
    if data.status_code == 200:
        print("Body response:")
        print("\t- type:", type(data.text))
        print("\t- content:", data.text)
