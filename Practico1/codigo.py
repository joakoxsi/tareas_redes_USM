import socket
import os 

################### Cliente UDP ###################

IP="1"
PUERTO_UDP=1
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
            print("logica")
            bormita = "¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 = DEC 25."
            socketUDP.send(bormita.encode())
            datos=socketUDP.recv(1024)
            print("Recibido: ",datos.decode())        
    else:
        print("¡¡Texto no reconocido!!") 

    
print("¡¡Final: esto es cine!!")