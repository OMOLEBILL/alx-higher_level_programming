#!/usr/bin/python3
import urllib.request
import sys
"""this module gets a specific value from the entered url"""


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers.get("X-Request-Id")
    print(x_request_id)
