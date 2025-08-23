import socket
from global_functions import *

host = "127.0.0.1"

# SERVICIO 1: Cliente TCP y Servidor TCP

PORT_1_2 = 5000
PORT_4_1 = 5006

flag=True

# CLiente TCP mandando a Servidor TCP
cliente_tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente_tcp.connect((host,PORT_1_2))
mensaje="115".encode('utf-8')
cliente_tcp.sendall(mensaje)

# Servidor TCP esperando
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.bind((host, PORT_4_1))
    #Escuchar conexiones: permitir conexiones entrantes
    s2.listen()

    #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
    while flag: 
        conn, addr = s2.accept() 
        with conn:
            print('Conectado por', addr)
            datos=b""
            while flag:
                data = conn.recv(1024*100) #Recibir hasta 1024 bytes, OJO con el tamaño del mensaje
                if not data:
                    break
                datos+=data
                print("Mensaje recibido:", datos.decode())
                if datos.decode() == "115":
                    mensajes=mensaje_inicials()
                    cliente_tcp.sendall(mensajes.encode())
                # Lógica de Finalización
                else:
                    partes = datos.decode().split("-")
                    if partes[len(partes)-1] == "FINALIZAR":
                        cliente_tcp.sendall(datos)
                        flag=False
                        break
                        
                    else:
                        mensajes=crear_mensaje(datos.decode())
                        cliente_tcp.sendall(mensajes.encode())
    
    cliente_tcp.close()
    print("Se cerró el servicio")