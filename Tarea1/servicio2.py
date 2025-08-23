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
    s.listen()

    while  flag: 
        conn, addr = s.accept() 
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024*100) #Recibir hasta 1024 bytes, OJO con el tamaño del mensa
                if not data:
                    break
                print("Mensaje recibido:", data.decode())
                
                # Lógica de Finalización
                partes = data.decode().split("-")
                if partes[-1] == "FINALIZAR":
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    sock.sendto(data, (host, PORT_2_3))   
                    flag=False
                    break
                
                if data.decode() != "115":
                    mensaje=crear_mensaje(data.decode())
                    sock.sendto(mensaje.encode(), (host, PORT_2_3))
                else:
                    mensaje=data.decode()
                    sock.sendto(mensaje.encode('utf-8'), (host, PORT_2_3))

        if not flag:
            break 

sock.close()
print("Se cerró el servicio")
