#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    # Get the info requesting the api
    user = sys.argv[1]
    passw = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(user)

    response = requests.get(url, auth=(user, passw))

    try:
        print(response.json()['id'])
    except KeyError:
        print("None")
