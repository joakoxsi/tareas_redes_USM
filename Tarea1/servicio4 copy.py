from global_functions  import *
import http.server
import socketserver
import threading
import datetime
import socket
import sys
import re

#import global_functions

# Variables globales para los hilos
mensaje = ""
largo_minimo = 0
flag = False

# Variables de configuracion 
host = "localhost"
PORT_3_4 = 8080
PORT_4_1 = 5006 

# Servidor HTTP
class HTTPServerHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        global mensaje, largo_minimo, flag

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"Mensaje recibido por HTTP: {post_data}")

        # Separamos las partes del mensaje

        if  post_data == "115" :
            mensaje = "115"

        else:
            parts = post_data.split('-')
            # Se valida el formato "[Timestamp]-[LargoMínimo]-[LargoActual]-[Mensaje]"
            if len(parts) == 4:
                timestamp_str = parts[0]
                largo_minimo = int(parts[1])
                largo_actual = int(parts[2])
                mensaje_body = parts[3]
            
                # Preparamos el mensaje para la siguiente iteración
                mensaje = mensaje_body
                    
                # Lógica para verificar el largo del mensaje
                if largo_actual >= largo_minimo:
                    # Si el largo excedio el minimo, guardamos el archivo y activamos la señal de finalización
                    print("El mensaje ha alcanzado la longitud mínima. Finalizando la cadena.")
                    file = f"mensaje_final_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
                    
                    with open(file, "w", encoding="utf-8") as file:
                        file.write(f"{timestamp_str}-{largo_minimo}-{largo_actual}-{mensaje_body}")
                    
                    flag = True
                    
                else:
                    # Si el largo no es suficiente, solicitamos una nueva palabra
                    print("El mensaje no ha alcanzado la longitud mínima. Continúa la cadena.")
                    
                    mensaje = crear_mensaje(post_data)
                    
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Mensaje recibido y procesado.".encode('utf-8'))

#Cliente TCP: 
def tcp_client():
    global mensaje, flag
    # Creamos el socket 
    tcp_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    
    # Bucle para enviar mensajes mientras no haya señal de finalización
    while not flag:
        # Esperamos a que el servidor HTTP haya procesado un mensaje
        if mensaje != "":
            # Creamos el nuevo mensaje con el formato solicitado
            print(115)
            if mensaje == "115":
                # Nos conectamos al Servicio 1
                tcp_socket.connect((host, PORT_4_1))
                print(f"Conectado a {host}:{PORT_4_1}")
                tcp_socket.sendall(mensaje.encode('utf-8'))
                print(f"Mensaje enviado a Servicio 1: {mensaje}")
            else:
                new_mensaje = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-{largo_minimo}-{len(mensaje.split())}-{mensaje}"
                
                # Envio mensaje servicio 1
                tcp_socket.sendall(new_mensaje.encode('utf-8'))
                print(f"Mensaje enviado a Servicio 1: {new_mensaje}")
                
        # Se limpia mensaje para nuevo ciclo 
        mensaje = ""
    
    # Finalizacion
    if flag:
        print("Finalizando conexiones y saliendo...")

        # Enviamos la señal de finalizacion al Servicio 1
        mensaje_final = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-FINALIZAR"

        tcp_socket.sendall(mensaje_final.encode('utf-8'))
        print("Señal de finalización enviada al Servicio 1.")
        
        sys.exit(0) # Salimos del programa

# Ejecucion principal
def main():
    # Inicio hilo del cliente TCP
    client_thread = threading.Thread(target=tcp_client) 
    client_thread.start()

    # Creamos el servidor HTTP y lo dejamos escuchando
    with socketserver.TCPServer(("", PORT_3_4), HTTPServerHandler) as httpd:
        print(f"Servidor HTTP del Servicio 4 escuchando en el puerto {PORT_3_4}")
        # El bucle del servidor se ejecuta en el hilo principal
        while not flag:
            httpd.handle_request()
            
    print("Servicio 4 finalizado.")

if __name__ == "__main__":
    main()