import time

print(time.time())
print(time.localtime())
print("testt")

# script.py

import requests

# Example: Make a GET request to a URL
response = requests.get('https://api.github.com')
print(response.json())