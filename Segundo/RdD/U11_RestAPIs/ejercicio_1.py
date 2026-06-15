import requests

r = requests.get("https://jsonplaceholder.typicode.com/users")
data = r.json()

for clave in data:
    print(clave['name'])
