import socket
import json

################### Cliente HTTP ###################

IP_SERVIDOR = "192.168.1.179"
PUERTO_HTTP = "9002"

while True:

    texto=input("Ingrese el comando")

    if texto=="POST":
    
        mensaje = input("Enviar solicitud HTTP: [frase]-[ID]")
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP_SERVIDOR, PUERTO_HTTP))
            request_body = mensaje.encode()
            print(request_body)
            request_headers = [
                            f"POST / H1TTP/1.1",
                            f"Host: {IP_SERVIDOR}:{PUERTO_HTTP}",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(request_body)}",
                            "Connection: close",
                            "\r\n"
            ]
            http_request = "\r\n".join(request_headers).encode() + request_body

        s.sendall(http_request)
        break

    else:
        print("Comando no reconocido")


print("¡¡Final: esto es cine!!")