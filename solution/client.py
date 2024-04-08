import requests

url = "http://localhost:8000/"

data = {
    "client": "Juan Perez",
    "status": "Pendiente",
    "payment": "Tarjeta de Crédito",
    "shipping": 10.0,
    "products": ["Camiseta", "Pantalón", "Zapatos"],
    "order_type": "Física"
}
ruta = url+"orders"
response = requests.request(method="POST",url=ruta, json=data)
print(response.text)


data = {
    "client": "Maria Rodriguez",
    "status": "Pendiente",
    "payment": "PayPal",
    "code": "ABC123",
    "expiration": "2022-12-31",
    "order_type": "Digital"
}
ruta = url+"orders"
response = requests.request(method="POST",url=ruta, json=data)
print(response.text)


data = {
    "client": "Ana Gutierrez",
    "status": "Pendiente",
    "payment": "Tarjeta de Débito",
    "shipping": 20.0,
    "products": ["Licuadora", "Refrigeradora", "Lavadora"],
    "order_type": "Física"
}
ruta = url+"orders"
response = requests.request(method="POST",url=ruta, json=data)
print(response.text)

ruta = url+"orders'"
response = requests.request(method="GET",url=ruta)
print(response.text)

ruta = url+"orders/?status='Pendiente'"
response = requests.request(method="GET",url=ruta)
print(response.text)

