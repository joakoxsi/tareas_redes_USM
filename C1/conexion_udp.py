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
            bromita = "¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 = DEC 25."
            socketUDP.send(bromita.encode()) #Envio del mensaje al servidor
            datos=socketUDP.recv(1024) #Recepcion de la respuesta del servidor
            print("Recibido: ",datos.decode()) #Impresion de la respuesta
    else:
        print("¡¡Texto no reconocido!!") 

    
print("¡¡Final: esto es cine!!")