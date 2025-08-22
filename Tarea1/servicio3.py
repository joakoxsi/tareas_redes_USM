import socket
from regla_mensaje import *

host="127.0.0.1"
puerto= 5005
print("Se inicio el servicio3")

flag=True

puerto_tcp=5006

servidor=  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind((host,puerto))

while flag:
    data, addr =servidor.recvfrom(1024)
    print(data)
    
    # CLiente TCP mandando a Servidor TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,puerto_tcp))
        
        if data.decode() == "115":
            mensaje="935"
        else:
            mensaje=crear_mensaje(data.decode())

        s.sendall(mensaje.encode())
        if data.decode() == "935":
            s.close()
            servidor.close()
            flag=False
            

        