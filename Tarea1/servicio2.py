import socket
import regla_mensaje
from regla_mensaje import *

# Configurar el host y puerto TCP
host = "127.0.0.1"
port = 5000

flag=True

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))

    #Escuchar conexiones: permitir conexiones entrantes
    s.listen()

    #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
    while  flag: 
        conn, addr = s.accept() 
        data=""
        with conn:
            print('Conectado por', addr)
            while  flag:
                data = conn.recv(1024) #Recibir hasta 1024 bytes, OJO con el tamaño del mensaje
                if not data:
                    break
                print("Mensaje recibido:", data.decode())

                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                if data.decode() != "935":
                    if data.decode() != "115":
                        mensaje=crear_mensaje(data.decode())
                    else:
                        mensaje=data.decode()

                    
                    sock.sendto(mensaje.encode('utf-8'), (UDP_IP, UDP_PORT))
                else:
                    s.close()
                    sock.sendto(data, (UDP_IP, UDP_PORT))
                    sock.close()
                    flag=False

print("Se cerro el servicio")
