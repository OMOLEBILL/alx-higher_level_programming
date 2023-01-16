#!/bin/bash
#check content length

# Get the URL from the first command line argument
url=$1

# Send the request to the URL using curl
response=$(curl -s -D - "$url" -o /dev/null)

# Extract the size of the body from the response headers
size=$(echo "$response" | grep -Fi Content-Length | awk '{print $2}')

# Print the size of the body in bytes
echo "$size"
