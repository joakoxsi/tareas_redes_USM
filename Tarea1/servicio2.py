import socket

from global_functions  import *

# Configurar el host y puerto TCP
host = "127.0.0.1"
TCP_PORT = 5000

flag=True

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, TCP_PORT))

    #Escuchar conexiones: permitir conexiones entrantes
    s.listen()

    #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
    while  flag: 
        conn, addr = s.accept() 
        datos=b""
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024) #Recibir hasta 1024 bytes, OJO con el tamaño del mensaje
  
                if not data:

                    break

                datos+=data

                if datos.decode() != "935":
                    if datos.decode() != "115":
                        mensaje=crear_mensaje(datos.decode())
                    else:
                        mensaje=datos.decode()

                    sock.sendto(mensaje.encode('utf-8'), (UDP_IP, UDP_PORT))
                else:
                    s.close()
                    sock.sendto(datos, (UDP_IP, UDP_PORT))
                    sock.close()
                    flag=False

                print("Mensaje recibido:", data.decode())


print("Se cerro el servicio")
