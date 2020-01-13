#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    # Get the info requesting the api
    url = 'https://swapi.co/api/people'
    params = (('search', sys.argv[1]),)
    r = requests.get(url, params=params)

    # Convert to json
    res = r.json()

    # Print the count key
    print("Number of results: {}".format(res['count']))

    # Isolate the characters that is a list
    # Print each one of the results
    characters = res['results']
    for c in characters:
        print(c['name'])
