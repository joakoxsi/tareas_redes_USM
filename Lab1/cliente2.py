import re,socket,asyncio,os,json

################### Cliente UDP ###################

IP="192.168.1.179"
PUERTO_UDP=9001
comando=["JOKE","EXIT"]

socketUDP=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketUDP.connect((IP,PUERTO_UDP))

while True:
    texto= input("Ingrese el texto a enviar: ")
    
    if texto in comando:

        if texto=="EXIT":
            print("Cerrando conexion")
            socketUDP.close()
            break
        
        elif texto=="JOKE":
            socketUDP.send(texto.encode())
            datos=socketUDP.recv(1024)
            print("Recibido: ",datos.decode())        
    else:
        print("¡¡Texto no reconocido!!") 

    
print("¡¡Final: esto es cine!!")


