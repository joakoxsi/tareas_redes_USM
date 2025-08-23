from global_functions  import *
import socket
import threading
import sys
import datetime
import re

#from global_functions import *

# Variables globales para los hilos
mensaje = ""
flag = False

# Variables de configuracion
host = "127.0.0.1" 
host_local = "localhost" # Dirección del servicio3 a Servicio4
PORT_2_3 = 5005
PORT_3_4 = 8080

mensaje_finalizar = "FINALIZAR"

# Servidor UDP
def udp_server():
    global mensaje, flag

    # Creamos un servidor UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, PORT_2_3))
        print(f"Servidor UDP del Servicio 3 escuchando en el puerto {PORT_2_3}")

        while not flag:
            # Esperamos datos
            data, addr = s.recvfrom(1024*100) 
            received_mensaje = data.decode('utf-8')
            print(f"Mensaje recibido por UDP: {received_mensaje}")
            
            
            # Separamos las partes del mensaje
            if received_mensaje == "115":
                mensaje="115"
            else:
                # Verificamos si es una señal de finalizacion
                if  mensaje_finalizar in received_mensaje:
                    print("Señal de finalización recibida. Propagando al siguiente servicio.")
                    flag = True
                    break # Salimos del bucle
                
                # Componemos el nuevo string con el formato "[Timestamp]-[LargoMínimo]-[LargoActual]-[Mensaje]"
                print("Procesando mensaje...")
                mensaje = crear_mensaje(received_mensaje)
                print(f"Mensaje procesado: {mensaje}")
                        
        s.close()
        sys.exit(0) # Salimos del programa

# Cliente HTTP
def http_client():
    global mensaje, flag
    
    # Bucle para enviar mensajes mientras no haya señal de finalización
    while not flag:
        # Esperamos a que el servidor UDP reciba un mensaje
        if mensaje != "":
            
            # Creación de un socket TCP para la solicitud HTTP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host_local, PORT_3_4))
                
                # Preparar la solicitud HTTP POST
                request_body = mensaje.encode('utf-8')
                print(request_body)
                request_headers = [
                    f"POST / HTTP/1.1",
                    f"Host: {host_local}:{PORT_3_4}",
                    "Content-Type: text/plain",
                    f"Content-Length: {len(request_body)}",
                    "Connection: close",
                    "\r\n"
                ]
                
                # Unir las cabeceras y el cuerpo de la solicitud
                http_request = "\r\n".join(request_headers).encode('utf-8') + request_body
                
                # Enviar la solicitud completa
                s.sendall(http_request)
                print("Solicitud HTTP POST enviada al Servicio 4.")
                
                # Recibir y mostrar la respuesta del servidor (borrar si es necesario)
                response = s.recv(4096).decode('utf-8')
                print(f"Respuesta del Servidor HTTP:\n{response}")
                    

            # Se limpia mensaje para nuevo ciclo 
            mensaje = ""
            response=""
            
    # Finalizacion
    if flag:
        print("Finalizando conexiones y saliendo...")
        # El Servicio 3 no propaga la señal, ya que la recibio
        # El programa termina
        sys.exit(0)

# Ejecucion principal
def main():
    # Hilos para el servidor UDP y el cliente HTTP
    server_thread = threading.Thread(target=udp_server)
    server_thread.start()

    client_thread = threading.Thread(target=http_client)
    client_thread.start()


    client_thread.join()
    server_thread.join()
    print("Servicio 3 finalizado.")

if __name__ == "__main__":
    main()