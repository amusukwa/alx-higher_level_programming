#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib.
"""

from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content:", content.decode('utf-8'))
