#!/bin/bash
#send a delete request
# Get the URL from the first command line argument
url=$1

# Send the DELETE request to the URL using curl
curl -s -X DELETE "$url"
