from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

# Configurar el host y puerto
host = "127.0.0.1"  # localhost
port = 8000

# Crear el servidor
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Servidor corriendo en http://{host}:{port}/")
server.serve_forever()  # Mantener el servidor activo

# SERVICIO 1: Cliente TCP y Servidor TCP

entrada = input("Ingrese el largo minimo: ")

# Enviar mensaje al servidor TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

####################################

# SERVICIO 2: Cliente UDP y Servidor TCP

####################################

# SERVICIO 3: CLiente HTTP y Servidor UDP

####################################

# SERVICIO 4: CLiente TCP y Servidor HTTP

####################################
