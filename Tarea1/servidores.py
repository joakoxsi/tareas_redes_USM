import socket

# Configurar el host y puerto TCP
host = "127.0.0.1"
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))

    #Escuchar conexiones: permitir conexiones entrantes
    s.listen()

    #Aceptar conexiones: espera hasta que alguien se conecte, devuelve el host y el port de la conexion
    conn, addr = s.accept() 

    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024) #Recibir hasta 1024 bytes, OJO con el tamaño del mensaje
            if not data:
                break
            print("Mensaje recibido:", data.decode())
    