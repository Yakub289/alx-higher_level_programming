#!/usr/bin/python3

"""script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response."""

import urllib.request as response
from sys import argv


if __name__ == "__main__":
    connect = response.Request(argv[1])
    with response.urlopen(connect) as response:
        print(response.headers.get('X-Request-Id'))
