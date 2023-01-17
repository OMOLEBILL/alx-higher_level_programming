#!/usr/bin/python3
"""this is a github module"""


if __name__ == "__main__":
    import requests
    import sys

    # Get the username and password passed as command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Set up the authentication for the request
    auth = (username, password)

    # Send the GET request to the GitHub API
    response = requests.get("https://api.github.com/user", auth=auth)

    # Try to parse the response as JSON
    data = response.json()

    # Print the user id
    print(data.get("id"))
