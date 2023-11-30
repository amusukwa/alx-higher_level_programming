#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1; curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r'
