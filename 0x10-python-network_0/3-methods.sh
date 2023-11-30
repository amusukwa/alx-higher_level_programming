#!/bin/bash
# Sends an OPTIONS request to the provided URL and displays allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep -i allow | cut -d ' ' -f 2-
