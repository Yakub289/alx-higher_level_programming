#!/usr/bin/python3

"""A script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    contact = {"email": sys.argv[2]}

    fetch = requests.post(url, data=contact)
    print(fetch.text)
