import socket

from global_functions  import *

# Configurar el host y puertos
host = "127.0.0.1"
PORT_1_2 = 5000
PORT_2_3 = 5005

flag=True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, PORT_1_2))

    #Escuchar conexiones: permitir conexiones entrantes
    s.listen()

    #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
    while  flag: 
        conn, addr = s.accept() 
        datos=b""
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024) #Recibir hasta 1024 bytes, OJO con el tamaño del mensa
                if not data:
                    break

                datos+=data

                if datos.decode() != "115":
                    mensaje=crear_mensaje(datos.decode())
                    sock.sendall(mensaje.encode())

                # Lógica de Finalización
                partes = datos.decode().split("-")
                if len(partes) > 1 and partes[1] == "FINALIZAR":

                    s.close()
                    sock.sendto(datos, (host, PORT_2_3))
                    sock.close()
                    flag=False

                else:
                    mensaje=datos.decode()

                    sock.sendto(mensaje.encode('utf-8'), (host, PORT_2_3))
                    

                print("Mensaje recibido:", data.decode())


print("Se cerro el servicio")
