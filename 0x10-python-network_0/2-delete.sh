#!/bin/bash
# This script sends a DELETE request to the provided URL and displays the body of the response
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1; curl -sX DELETE "$1"
