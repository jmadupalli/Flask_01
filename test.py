import requests

BASE = "http://localhost:5000/"

data = [
{"name": "Video 4", "likes":10, "views":0},
{"name": "Video 2", "likes":10, "views":0},
{"name": "Video 3", "likes":10, "views":0},
]

for i in range(len(data)):
    response = requests.put(BASE+'video/'+str(i), data[i])
    print(response.json())
input()
response = requests.patch(BASE+'/video/2', {"views":100, "likes":230})
print(response.json())
