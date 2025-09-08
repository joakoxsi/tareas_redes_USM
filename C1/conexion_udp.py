import re,socket,asyncio,os,json

################### Cliente UDP ###################

IP="192.168.1.179" #El profe debe especificar el IP
PUERTO_UDP=9001 #El profe debe especificar el puerto
comando=["JOKE","EXIT"]

socketUDP=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creacion del socket UDP
socketUDP.connect((IP,PUERTO_UDP)) #Conexion al servidor

while True:
    texto= input("Ingrese el texto a enviar: ")
    
    if texto in comando:

        if texto=="EXIT":
            print("Cerrando conexion")
            socketUDP.close() #Cierre del socket
            break
        
        elif texto=="JOKE":
            socketUDP.send(texto.encode()) #Envio del comando JOKE
            datos=socketUDP.recv(1024) #Recepcion de datos (max 1024 bytes)
            print("Recibido: ",datos.decode()) #Impresion de los datos recibidos   
    else:
        print("¡¡Texto no reconocido!!") 

    
print("¡¡Final: esto es cine!!")