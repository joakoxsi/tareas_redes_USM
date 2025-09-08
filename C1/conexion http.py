import socket
import json

################### Cliente HTTP ###################

IP_SERVIDOR = "192.168.1.179"
PUERTO_HTTP = "9002"

while True:

    texto=input("Ingrese el comando")

    if texto=="POST":
    
        mensaje = input("Enviar solicitud HTTP: [frase]-[ID]")
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #se crea el socket TCP
            s.connect((IP_SERVIDOR, PUERTO_HTTP)) #se conecta al servidor
            request_body = mensaje.encode() #se codifica el mensaje

            request_headers = [ #se crean las cabeceras
                            f"POST / HTTP/1.1",
                            f"Host: {IP_SERVIDOR}:{PUERTO_HTTP}",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(request_body)}",
                            "Connection: close",
                            "\r\n"
            ]
            http_request = "\r\n".join(request_headers).encode() + request_body #se crea la solicitud HTTP

        s.sendall(http_request) #se envía la solicitud al servidor
        response = s.recv(4096).decode('utf-8') #se recibe la respuesta del servidor
        print(f"Respuesta del Servidor HTTP:\n{response}")
        break

    else:
        print("Comando no reconocido")


print("¡¡Final: esto es cine!!")