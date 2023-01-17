#!/usr/bin/python3
import urllib.request
"""This module importa url and checks it's status"""


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    data = response.read()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode("utf-8"))
