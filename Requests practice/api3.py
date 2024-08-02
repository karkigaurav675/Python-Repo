# https://api.sampleapis.com/playstation/games
import requests
import json
response = requests.get("https://api.sampleapis.com/playstation/games")
# print(response.text)
print(response.status_code)
data = response.json()
print(json.dumps(data, indent=4))