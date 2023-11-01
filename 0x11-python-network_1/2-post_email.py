#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_data = {'email': email}
    email_data_encoded = urllib.parse.urlencode(email_data).encode('utf-8')

    req = urllib.request.Request(url, method="POST", data=email_data_encoded)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
