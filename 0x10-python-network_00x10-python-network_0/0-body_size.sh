#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the provided URL and display the size of the response body
response_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r')

if [ -z "$response_size" ]; then
    echo "Failed to retrieve response size."
else
    echo  "${response_size}"
fi
