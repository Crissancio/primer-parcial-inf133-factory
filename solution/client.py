import requests

url = "http://localhost:8000/"

ruta = url+"orders"
response = requests.request(method="GET",url=ruta)

print(response.text)