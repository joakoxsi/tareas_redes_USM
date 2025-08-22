import socket
import threading
import sys
import datetime
import re

#from global_functions import *

# Variables globales para los hilos
MESSAGE = ""
TERMINATE_SIGNAL = False

# Variables de configuracion
HOST_SERVICE_3 = "localhost" # ojo, sino -> "0.0.0.0"
PORT_SERVICE_3 = 5005        # Puerto del Servidor UDP

HOST_SERVICE_4 = "localhost" # Dirección del Servidor HTTP de Servicio4
PORT_SERVICE_4 = 8080


TERMINATION_MESSAGE = "FINALIZAR"
flag=True

puerto_tcp=5006

# Servidor UDP
def udp_server():
    global MESSAGE, TERMINATE_SIGNAL

    # Creamos un socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST_SERVICE_3, PORT_SERVICE_3))
        print(f"Servidor UDP del Servicio 3 escuchando en el puerto {PORT_SERVICE_3}")

        while not TERMINATE_SIGNAL:
            # Esperamos datos
            data, addr = s.recvfrom(1024) 
            received_message = data.decode('utf-8')
            print(f"Mensaje recibido por UDP: {received_message}")
            
            # Verificamos si es una señal de finalización
            if TERMINATION_MESSAGE in received_message:
                print("Señal de finalización recibida. Propagando al siguiente servicio.")
                TERMINATE_SIGNAL = True
                break # Salimos del bucle
            
            # Separamos las partes del mensaje
            parts = received_message.split('-')
            
            # Si el formato es correcto, procesamos el mensaje
            if len(parts) == 4:
                timestamp_str, min_length_str, current_length_str, message_body = parts
                
                new_word = input("Ingresa una nueva palabra para el mensaje: ")
                
                # Agregamos la nueva palabra y actualizamos la longitud
                updated_message_body = f"{message_body} {new_word}"
                updated_length = len(updated_message_body.split())
                
                # Componemos el nuevo string con el formato "[Timestamp]-[LargoMínimo]-[LargoActual]-[Mensaje]"
                MESSAGE = f"{timestamp_str}-{min_length_str}-{updated_length}-{updated_message_body}"
                       
        s.close()
        sys.exit(0) # Salimos del programa

# Cliente HTTP
def http_client_logic():
    global MESSAGE, TERMINATE_SIGNAL
    
    # Bucle para enviar mensajes mientras no haya señal de finalización
    while not TERMINATE_SIGNAL:
        # Esperamos a que el servidor UDP reciba un mensaje
        if MESSAGE != "":
            
            # Creación de un socket TCP para la solicitud HTTP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST_SERVICE_4, PORT_SERVICE_4))
                
                # Preparar la solicitud HTTP POST
                request_body = MESSAGE.encode('utf-8')
                request_headers = [
                    f"POST / HTTP/1.1",
                    f"Host: {HOST_SERVICE_4}:{PORT_SERVICE_4}",
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
            MESSAGE = ""
            
    # Finalizacion
    if TERMINATE_SIGNAL:
        print("Finalizando conexiones y saliendo...")
        # El Servicio 3 no propaga la señal, ya que la recibio
        # El programa termina
        sys.exit(0)

# Ejecucion principal
def main():
    # Creamos e iniciamos los hilos para el servidor UDP y el cliente HTTP
    server_thread = threading.Thread(target=udp_server_logic)
    server_thread.start()

    client_thread = threading.Thread(target=http_client_logic)
    client_thread.start()

    # Mantenemos el hilo principal vivo esperando a que los otros terminen
    server_thread.join()
    client_thread.join()
    
    print("Servicio 3 finalizado.")

if __name__ == "__main__":
    main()