import re,socket,asyncio,os,json

################### Cliente TCP ###################

IP="192.168.1.179"
PUERTO_TCP=9000
comando=["GET","JOKE","EXIT"]

socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketTCP.connect((IP,PUERTO_TCP))

while True:
    texto= input("Ingrese el texto a enviar: ")
    
    if texto in comando:

        if texto=="EXIT":
            print("Cerrando conexion")
            socketTCP.close()
            break
        
        elif texto=="GET" or texto=="JOKE":
            socketTCP.send(texto.encode())
            datos=socketTCP.recv(1024)
            print("Recibido: ",datos.decode())   
    else:
        print("¡¡Texto no reconocido!!") 

    
print("¡¡Final: esto es cine!!")


