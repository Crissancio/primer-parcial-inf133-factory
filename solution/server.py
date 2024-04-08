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

'''class OrdenFisica(self):
    super().__init__():'''
    
        
ordenes = {}

class OrdenesService:
    @staticmethod
    def find_order(id):
        print()
        return ordenes[id]
        
    
    @staticmethod
    def add_order(data):
        if len(ordenes)==0:
            ordenes[1] = data
        else:
            index = ordenes.keys()
            index = int(max(list(index)))+1
            ordenes[index] = data
        return data
    
    @staticmethod
    def filter_by_status(status):
        return [
            orden for orden in ordenes
            if orden["status"] == status
        ]
    
    @staticmethod
    def update_order(id, data):
        order = OrdenesService.find_order(id)
        if order:
            order.update(data)
            return orders
        else:
            return None
        
class ResponseHandler:
    @staticmethod
    def response_handler(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class RESTfulRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        if parsed_path.path == '/orders':
            if "status" in query_params:
                status = query_params["status"][0]
                print(status)
                ordenes_filtradas= OrdenesService.filter_by_status(status)
                ResponseHandler.response_handler(self, 200, ordenes_filtradas)
            else:
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
        httpd = HTTPServer(server_address,RESTfulRequestHandler)
        print(f"Iniciando servidor HTTP en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()