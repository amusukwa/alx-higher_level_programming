#!/bin/bash
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1
curl -sI "$1" | grep -i content-length | awk '{ "$2"}' | tr -d '\r'
