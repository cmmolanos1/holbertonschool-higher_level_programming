#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    post_url = sys.argv[1]
    post_data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf8')

    with urllib.request.urlopen(url=post_url, data=post_data) as response:
        posted = response.read()

    print(posted.decode('utf8'))
