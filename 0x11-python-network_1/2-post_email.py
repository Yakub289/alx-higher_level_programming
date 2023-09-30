#!/usr/bin/python3

"""A script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""


import urllib.parse as parse
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    contact = {'email': argv[2]}
    data = parse.urlencode(contact).encode('utf-8')
    fetch = request.Request(argv[1], data)
    with request.urlopen(fetch) as personnel:
        print(personnel.read().decode('utf-8'))
