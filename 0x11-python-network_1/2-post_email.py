#!/usr/bin/python3
"""
script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response
"""


from urllib import request
from urllib import parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = {'email': email}
    data_encoded = parse.urlencode(data).encode('ascii')

    with request.urlopen(url, data=data_encoded) as response:
        print(response.read().decode('utf-8'))
