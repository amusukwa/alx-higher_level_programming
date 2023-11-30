#!/bin/bash

URL=$1

# Send a GET request and display the body of the response for a 200 status code
curl -s -X GET -L "$URL"
