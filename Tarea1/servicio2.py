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
                data = conn.recv(1024*100) #Recibir hasta 1024 bytes, OJO con el tamaño del mensa
                if not data:
                    break

                datos+=data
                print("Mensaje recibido:", data.decode())
                if datos.decode() != "115":
                    mensaje=crear_mensaje(datos.decode())
                    sock.sendto(mensaje.encode(), (host, PORT_2_3))

                # Lógica de Finalización
                partes = datos.decode().split("-")
                if partes[-1] == "FINALIZAR":

                    sock.sendto(datos, (host, PORT_2_3))   
                    flag=False
                    break

                else:
                    mensaje=datos.decode()
                    sock.sendto(mensaje.encode('utf-8'), (host, PORT_2_3))

        if not flag:
            break 

sock.close()
print("Se cerró el servicio")
