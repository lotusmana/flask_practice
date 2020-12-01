import requests

BASE = "http://localhost:5003/"

response = requests.patch(BASE + "video/2", {"views":333, "likes":111})
print(response.json())

# data = [{"likes": 10000, "name": "Mindflower Horoscope", "views":50000},
#         {"likes": 100, "name": "Mindflower ", "views":99000},
#         {"likes": 10, "name": "Mind FLOWER", "views":5000}]

# for i in range(4,7):
#     response = requests.put(BASE + "video/" + str(i), data[i - 4])
#     print(response.json())

# #input()

# #response = requests.delete(BASE + "video/0")
# #print(response)

# input()

# response = requests.get(BASE + "video/9")
# print(response.json())