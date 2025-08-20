from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

'''
# Configurar el host y puerto
host = "127.0.0.1"  # localhost
port = 5000

# Crear el servidor
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Servidor corriendo en http://{host}:{port}/")
server.serve_forever()  # Mantener el servidor activo
'''
host = "127.0.0.1"

# SERVICIO 1: Cliente TCP y Servidor TCP

port_tcp = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port_tcp))
    s.sendall(b"Hola, servidor TCP")
    data = s.recv(1024)

print(f"Respuesta del servidor: {data.decode()}")

####################################

# SERVICIO 2: Cliente UDP y Servidor TCP

####################################

# SERVICIO 3: CLiente HTTP y Servidor UDP

####################################

# SERVICIO 4: CLiente TCP y Servidor HTTP

####################################
