import requests

try:
    r = requests.get('https://jsonplaceholder.typicode.com/invalid-endpoint')
    resultado = r.raise_for_status()
    print(r.text)

except requests.exceptions.HTTPError as err:
    print(f"Error {err}: La página no se encontró")

