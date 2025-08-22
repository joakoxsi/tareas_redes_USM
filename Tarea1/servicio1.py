import socket
from regla_mensaje import *

host = "127.0.0.1"

# SERVICIO 1: Cliente TCP y Servidor TCP

port_tcp = 5000
puerto=5006

flag=True

# CLiente TCP mandando a Servidor TCP
cliente_tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente_tcp.connect((host,port_tcp))
mensaje="115".encode('utf-8')
cliente_tcp.sendall(mensaje)

# Servidor TCP esperando
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.bind((host, puerto))
    #Escuchar conexiones: permitir conexiones entrantes
    s2.listen()

    #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
    while flag: 
        conn, addr = s2.accept() 
        data=""
        with conn:
            print('Conectado por', addr)
            while flag:
                data = conn.recv(1024) #Recibir hasta 1024 bytes, OJO con el tamaño del mensaje
                if not data:
                    break
                print("Mensaje recibido:", data.decode())
                print(data)
                if data.decode() != "935":
                    if data.decode() == "115":
                        mensajes=mensaje_inicials()

                    else:
                        mensajes=crear_mensaje(data.decode())

                    cliente_tcp.sendall(mensajes.encode())
                else:
                    s2.close()
                    cliente_tcp.sendall(data)
                    cliente_tcp.close()
                    flag=False


print("Se cerro el servicio")