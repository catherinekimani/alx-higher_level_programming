#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL & displays
the value of the X-Request-Id variable found in the header of the response.
"""


from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print("{}".format(html))
