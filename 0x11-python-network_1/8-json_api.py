#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 2:
        q_data = {'q': sys.argv[1]}
    else:
        q_data = {'q': ""}

    response = requests.post(url, data=q_data)

    try:
        json_data = response.json()

        if json_data:
            print(f"{[json_data['id']]} {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
