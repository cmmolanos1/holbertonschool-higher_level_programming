#!/usr/bin/python3
"""
Shows the caracter name
use pagination
"""

import requests
import sys

if __name__ == "__main__":
    # Get the info requesting the api
    url = 'https://swapi.co/api/people'
    params = (('search', sys.argv[1]),)
    page = 1
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

        films = c['films']
        for film in films:
            print("\t{}".format(requests.get(film).json()['title']))

    # Loop for reading next pages
    while res['next'] is not None:
        res = requests.get(res['next']).json()
        characters = res['results']
        for c in characters:
            print(c['name'])

            films = c['films']
            for film in films:
                print("\t{}".format(requests.get(film).json()['title']))
