#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response.
curl -sI "$1" | head -n 1 | cut -d' ' -f 2
