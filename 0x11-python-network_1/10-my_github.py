#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and password)
and uses the GitHub API to display the user id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("Invalid credentials or insufficient permissions")
