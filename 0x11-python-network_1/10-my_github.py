#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    user_data = response.json()
    print(user_data.get('id'))
