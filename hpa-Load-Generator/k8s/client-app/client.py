import requests

url = "http://localhost:8080"

r = requests.get(url=url)
print(r.text)