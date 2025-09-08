import re,socket,asyncio,os,json

################### Cliente TCP ###################

IP="192.168.1.179" #El profe debe especificar el IP
PUERTO_TCP=9000 #El profe debe especificar el puerto
comando=["GET","JOKE","EXIT"]

socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Creacion del socket TCP
socketTCP.connect((IP,PUERTO_TCP)) #Conexion al servidor

while True:
    texto= input("Ingrese el texto a enviar: ")
    
    if texto in comando:

        if texto=="EXIT":
            print("Cerrando conexion")
            socketTCP.close() #Cierre del socket
            break
        
        elif texto=="GET":
            socketTCP.send(texto.encode()) #Envio del comando GET
            datos=socketTCP.recv(1024) #Recepcion de datos (max 1024 bytes)
            print("Recibido: ",datos.decode()) #Impresion de los datos recibidos

        elif texto=="JOKE":
            socketTCP.send(texto.encode())
            datos=socketTCP.recv(1024)
            print("Recibido: ",datos.decode())    
    else:
        print("¡¡Texto no reconocido!!") 

    
print("¡¡Final: esto es cine!!")
