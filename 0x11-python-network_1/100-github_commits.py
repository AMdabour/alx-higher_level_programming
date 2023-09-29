#!/usr/bin/python3
""" a Python script that takes 2 arguments to list the latest 10 commits"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    response = requests.get(url)

    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
