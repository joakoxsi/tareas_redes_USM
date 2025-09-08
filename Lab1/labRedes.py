import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# se especifican las direcciones tanto del cliente TCP como del servidor TCP
ClienteTCP = ("192.168.1.179", 9000) 
clienteUDP = ("192.168.1.179",9001)
clienteHTTP = ("192.168.1.179",1080)

#funcion main()
# Se realizan todas las gestiones que tiene que realizar el servicio 1, comenzando por pedir los datos de inicializacion como son
# el largo minimo y la palabra inicial, crea el servidor TCP para recibir de S4 y tambien se preocupa de enviar a S2 , de igual manera
# si se propaga la finalizacion este de igual manera propaga y se cierra además de enviar mensajes si es que fuese necesario.
def main():
    palabra = input("Inserte comando : ").strip()
    msg = palabra.strip()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        c.connect(ClienteTCP)
        c.sendall(msg.encode("utf-8"))
        respuesta=c.recv(1024)

    if(msg == "JOKE"):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as d:
            d.sendto(respuesta, clienteUDP)
            respuesta=d.recv(65536)
            print(respuesta.decode())
        
        respuesta= respuesta.decode()+", Grupo03"
        print("respuesta enviada ",respuesta)
        respuesta.encode("utf-8")
        request = (
            "POST /frase/ HTTP/1.1\r\n"
            f"Host: {clienteHTTP[0]}:{clienteHTTP[1]}\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            f"Content-Length: {len(respuesta)}\r\n"
            "Connection: close\r\n\r\n"
            f"{respuesta}" )
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(clienteHTTP)
            s.sendall(request.encode("utf-8"))
            resp = s.recv(65536)  
            print(resp)

    else:
        print(respuesta.decode())


if __name__ == "__main__":
    main()
