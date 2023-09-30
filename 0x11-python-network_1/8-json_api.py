#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user withthe letter as a parameter.
"""


import requests
from sys import argv

if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        parse_res = response.json()
        if parse_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(parse_res.get(
                "id"), parse_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
