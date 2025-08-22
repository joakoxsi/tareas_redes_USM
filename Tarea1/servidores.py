import socket

# Configurar el host y puerto TCP
host = "127.0.0.1"
port = 5006
contador=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    while True:
        

        #Escuchar conexiones: permitir conexiones entrantes
        s.listen()

        #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
        conn, addr = s.accept() 

        with conn:
            print('Conectado por', addr)
            datos=b""
            while True:
                data = conn.recv(206) #Recibir hasta 1024 bytes, OJO con el tamaño del mensaje
                contador+=1
                print(data,not data)
                if not data:
                    print(data)
                    print("llegamos")
                    break
                datos+=data
            print("Mensaje recibido:", datos.decode())
            print(contador)