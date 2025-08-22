import socket
from global_functions import *

host="127.0.0.1"
puerto= 5005
print("Se inicio el servicio3")

flag=True

puerto_tcp=5006

servidor=  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind((host,puerto))

while flag:

    datos=b""
    while flag:
        data, x=servidor.recvfrom(1024)

        if not data:
            break
        datos+=data
        # CLiente TCP mandando a Servidor TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host,puerto_tcp))
            
            if datos.decode() == "115":
                mensaje="115"
            else:
                mensaje=crear_mensaje(datos.decode())

            s.sendall(mensaje.encode())
            if datos.decode() == "935":
                s.close()
                servidor.close()
                flag=False
                

        