import socket
import json

################### Cliente HTTP ###################

IP_SERVIDOR = "192.168.1.179"
PUERTO_HTTP = 1080

ID = input("Identificador de grupo: ")
frase = "Recuerda: la realidad es relativa a la perspectiva."
mensaje = frase + "   " + ID

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP_SERVIDOR, PUERTO_HTTP))
    request_body = mensaje.encode()
    print(request_body)
    request_headers = [
                    f"POST /frase/ HTTP/1.1",
                    f"Host: {IP_SERVIDOR}:{PUERTO_HTTP}",
                    "Content-Type: text/plain",
                    f"Content-Length: {len(request_body)}",
                    "Connection: close",
                    "\r\n"
    ]
    http_request = "\r\n".join(request_headers).encode('utf-8') + request_body

    s.sendall(http_request)
    print("Solicitud HTTP POST enviada")

print("Fino seÃ±ores")