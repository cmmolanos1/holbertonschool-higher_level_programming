#!/bin/bash
# send a GET request to the URL, and displays the body of the response.
curl -s "$1" -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
