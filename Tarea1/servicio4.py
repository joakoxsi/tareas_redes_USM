import http.server
import socketserver
import threading
import datetime
import socket
import sys
import re

#import global_functions

# Variables globales para los hilos
MESSAGE = ""
MIN_LENGTH = 0
TERMINATE_SIGNAL = False

# Variables de configuracion 
HOST_SERVICE_1 = "localhost"
PORT_SERVICE_1 = 5006 
PORT_SERVICE_4 = 8080

# Servidor HTTP
class HTTPServerHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        global MESSAGE, MIN_LENGTH, TERMINATE_SIGNAL

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"Mensaje recibido por HTTP: {post_data}")

        # Separamos las partes del mensaje
        parts = post_data.split('-')
        
        # Se valida el formato "[Timestamp]-[LargoMínimo]-[LargoActual]-[Mensaje]"
        if len(parts) == 4:
            timestamp_str = parts[0]
            MIN_LENGTH = int(parts[1])
            current_length = int(parts[2])
            message_body = parts[3]
        
            # Preparamos el mensaje para la siguiente iteración
            MESSAGE = message_body
                
            # Lógica para verificar el largo del mensaje
            if current_length >= MIN_LENGTH:
                # Si el largo excedio el minimo, guardamos el archivo y activamos la señal de finalización
                print("El mensaje ha alcanzado la longitud mínima. Finalizando la cadena.")
                filename = f"mensaje_final_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
                
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(f"{timestamp_str}-{MIN_LENGTH}-{current_length}-{message_body}")
                
                TERMINATE_SIGNAL = True
                
            else:
                # Si el largo no es suficiente, solicitamos una nueva palabra
                print("El mensaje no ha alcanzado la longitud mínima. Continúa la cadena.")
                new_word = input("Ingresa una nueva palabra para el mensaje: ")
                
                MESSAGE += f"{new_word}" # Agregamos la nueva palabra
                
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Mensaje recibido y procesado.".encode('utf-8'))

#Cliente TCP: 
def tcp_client():
    global MESSAGE, TERMINATE_SIGNAL

    # Bucle para enviar mensajes mientras no haya señal de finalización
    while not TERMINATE_SIGNAL:
        # Esperamos a que el servidor HTTP haya procesado un mensaje
        if MESSAGE != "":
            # Creamos el nuevo mensaje con el formato solicitado
            new_message = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-{MIN_LENGTH}-{len(MESSAGE.split())}-{MESSAGE}"
            # Creamos el socket y nos conectamos al Servicio 1
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST_SERVICE_1, PORT_SERVICE_1))
                print(f"Conectado a {HOST_SERVICE_1}:{PORT_SERVICE_1}")
                
                s.sendall(new_message.encode('utf-8'))
                print(f"Mensaje enviado a Servicio 1: {new_message}")
            
            # Se limpia mensaje para nuevo ciclo 
            MESSAGE = ""
    
    # Finalizacion
    if TERMINATE_SIGNAL:
        print("Finalizando conexiones y saliendo...")

        # Enviamos la señal de finalizacion al Servicio 1
        termination_msg = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-FINALIZAR"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST_SERVICE_1, PORT_SERVICE_1))
                s.sendall(termination_msg.encode('utf-8'))
                print("Señal de finalización enviada al Servicio 1.")
        
        sys.exit(0) # Salimos del programa

# Ejecucion principal
def main():
    # Inicio hilo del cliente TCP
    client_thread = threading.Thread(target=tcp_client)
    client_thread.start()

    # Creamos el servidor HTTP y lo dejamos escuchando
    with socketserver.TCPServer(("", PORT_SERVICE_4), HTTPServerHandler) as httpd:
        print(f"Servidor HTTP del Servicio 4 escuchando en el puerto {PORT_SERVICE_4}")
        # El bucle del servidor se ejecuta en el hilo principal
        while not TERMINATE_SIGNAL:
            httpd.handle_request()
            
    print("Servicio 4 finalizado.")

if __name__ == "__main__":
    main()