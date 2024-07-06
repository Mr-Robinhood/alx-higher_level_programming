#!/usr/bin/python3
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=HTTPBasicAuth(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(f"Error: {response.status_code}")
