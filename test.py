import requests

BASE = "http://localhost:5003/"

response = requests.get(BASE + "helloworld")
print(response.json)
