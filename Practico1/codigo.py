import os, json, socket, re

IP_SERVER = "jdiaz.lat"
PORT = 50005

#expresion = re.compile(r"(.+,.+,.+)")

#Creacion del socket UDP
socketUDP=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
socketUDP.connect((IP_SERVER,PORT))

#conexion con server UDP

mensaje = "Hola mundo desde grupo 14"
socketUDP.send(mensaje.encode())

datos = socketUDP.recv(1024)
datos = datos.decode()
datos = datos[1:-1] #saca los primeros corchetes
print(datos)

lista_datos = datos.strip().split(";")
print(lista_datos)    

socketUDP.close()

imagen = b""

#trbajar los nodos
for info_nodo in lista_datos:
    info_nodo = info_nodo[1:-1]
    print(info_nodo)
    lista_info_nodo = info_nodo.split(",")
    print(lista_info_nodo) 

    (url, puerto, protocolo, codigo) = lista_info_nodo
    print(f"url: {url}, puerto: {puerto}, protocolo: {protocolo}, codigo: {codigo}")

    if protocolo == "TCP":
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            print(protocolo,(url,int(puerto)))
            s.connect((url,int(puerto)))
            s.sendall(f"14,{codigo}".encode())
            print(protocolo,(url,int(puerto)))
            data=s.recv(4096)
            imagen += data

    else:
        print(protocolo)
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
            s.bind((url,int(puerto)))  
            s.send(f"14, {codigo}".encode()) 
            data=s.recv(4096)
            imagen+= data

print(imagen)

with open("resultado.bin", 'wb') as archivo:
    archivo.write(imagen)