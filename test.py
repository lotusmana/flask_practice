import requests

BASE = "http://localhost:5003/"

response = requests.get(BASE + "helloworld/toby/31")
print(response.json())

