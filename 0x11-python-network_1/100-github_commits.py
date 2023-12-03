#!/usr/bin/python3
"""
Scrip takes 2 arguments in order to solve a challenge.
The first argument will be the repository name.
The second argument will be the owner name.
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    try:
        commits = response.json()
        for i, commit in enumerate(commits[:10]):
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            message = commit.get('commit').get('message')
            print(f"Commit {i + 1}: {sha} by {author}: {message}")
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("Invalid repository or owner name")
