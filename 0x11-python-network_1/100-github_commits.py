#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)

    params = {'per_page': 10}

    response = requests.get(url, params=params)

    commits = response.json()
    for commit in commits:
        commit_data = commit['commit']
        sha = commit['sha']
        author = commit_data['author']['name']
        print(f"{sha}: {author}")
