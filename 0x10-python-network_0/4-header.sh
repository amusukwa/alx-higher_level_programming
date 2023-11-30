#!/bin/bash
# This script sends a GET request to a URL with a specific header
curl -s -H "X-School-User-Id: 98" "$1"
