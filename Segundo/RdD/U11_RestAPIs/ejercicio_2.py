import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

print(r.text)

