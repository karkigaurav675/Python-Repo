import requests
response = requests.get("https://api.sampleapis.com/codingresources/codingResources")
# print(response.text)
# print(response.status_code)
# data = response.json()
# print(json.dumps(data, indent=2))

data = response.json()
for meeting in data:
    if meeting["types"]==["meeting"]:
        print(meeting)