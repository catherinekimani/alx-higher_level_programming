#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=auth)

    print(response.json().get("id"))
