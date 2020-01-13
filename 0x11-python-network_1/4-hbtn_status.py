#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status using REQUESTS """

import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    text = response.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
