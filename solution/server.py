from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
class Orden:
    def __init__(self, id, client, status, payment, shipping, type):
        self.id = id
        self.client=client
        self.status=status
        self.payment=payment
        self.order_type = type
    def type_order(self):
        print()

#class Order
        
ordenes = {
            "1": {
                "client": "Juan Perez",
                "status": "Pendiente",
                "payment": "Tarjeta de Crédito",
                "shipping": 10.0,
                "products": ["Camiseta", "Pantalón", "Zapatos"],
                "order_type": "Física"
            },
            "2":{
                "client": "Maria Rodriguez",
                "status": "Pendiente",
                "payment": "PayPal",
                "code": "ABC123",
                "expiration": "2022-12-31",
                "order_type": "Digital"
            }
        }

class OrdenesService:
    @staticmethod
    def add_order(data):
        id = ordenes['id'][-1] + 1
        data['id']=id
        ordenes.append(data)
        return data
        
class ResponseHandler:
    @staticmethod
    def response_handler(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class RESTfulRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/orders':
            '''if "status" in query_params:
                status = query_params["status"][0]
                ResponseHandler.response_handler(self, 200, ordenes)
            else:'''
            ResponseHandler.response_handler(self, 200, ordenes)
        else:
            ResponseHandler.response_handler(self, 404, ordenes)
    
    def do_POST(self):
        if self.path == '/orders':
            data = self.read_data()
            orden = OrdenesService.add_order(data)
            ResponseHandler.response_handler(self, 201, orden)
        else:
            ResponseHandler.response_handler(self, 404, ordenes)
            
    #def do_PUT(self)
        
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
            
            
    

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address,port)
        print(f"Iniciando servidor HTTP en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()