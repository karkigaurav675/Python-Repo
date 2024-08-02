import requests
import json
response = requests.get("https://api.sampleapis.com/coffee/hot")
# # print(response)
# # print(response.status_code)
# if response.status_code == 200:
#     print("Response is success.")
# else:
#     print("Response has failed.")
# print()
# # print(response.text)
# # print(response.json())
# data = response.json()
# print(json.dumps(data, indent=2))

data = response.json()
cappuccino = None
for coffee in data:
    if coffee.get('title') == 'Cappuccino':
        cappuccino = coffee
print(json.dumps(cappuccino))