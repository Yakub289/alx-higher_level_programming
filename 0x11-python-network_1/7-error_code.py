#!/usr/bin/python3

"""A script that takes in a URL, sends a request to the URL
and displays the body of the response."""

import requests
from sys import argv


if __name__ == '__main__':
    fetch = requests.get(argv[1])
    if fetch.status_code >= 400:
        print("Error code: {}".format(fetch.status_code))
    else:
        print(fetch.text)
