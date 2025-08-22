import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import global_functions

# Configuración global
CONFIG = {
    "http_port": 8080,
    "next_host": "127.0.0.1",
    "next_port": 5000,
}

def enviar_por_tcp(texto: str):
    """Conecta por TCP al siguiente servicio (Servicio 1) y envía el texto en UTF-8"""
    host = CONFIG["next_host"]
    port = CONFIG["next_port"]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(texto.encode("utf-8"))
        # Intentar leer una respuesta del servicio 1 (si es necesario)
        s.settimeout(0.5)
        #Asumimos que siempre recibe respuesta
        _ = s.recv(1024)

class Servicio4Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_POST(self):
        """Maneja el POST recibido"""
        # Leer el cuerpo del mensaje
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8", errors="replace").strip()

        print("\n=== POST recibido en", self.path, "===")
        print("Cuerpo:", body)

        #Interpretar el mensaje del servicio 3
        info = parsear_string(body)
        if info:
            print(f"Mensaje actual ({info['cur_len']} palabras): \"{info['msg']}\" | mínimo: {info['min_len']}")
            extra = input("Palabra extra a agregar (ENTER para no agregar): ").strip()
            if extra:
                nuevo_msg = info["msg"] + " " + extra
            else:
                nuevo_msg = info["msg"]