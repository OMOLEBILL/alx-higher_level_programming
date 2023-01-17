#!/usr/bin/python3
"""this module gets a specific value from the entered url"""

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)
