#!/usr/bin/python3
"""
Show the last 10 commits of rails repository
"""

import requests
import sys

if __name__ == "__main__":
    # Get the info requesting the api
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    commits = requests.get(url).json()

    for i in range(10):
        sha = commits[i]['sha']
        author = commits[i]['commit']['author']['name']
        print("{}: {}".format(sha, author))
