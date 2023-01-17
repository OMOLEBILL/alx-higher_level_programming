#!/usr/bin/python3
import urllib.request
import sys
"""this module gets a specific value from the entered url"""


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    header = response.info()
    print(header.get("X-Request-Id"))
