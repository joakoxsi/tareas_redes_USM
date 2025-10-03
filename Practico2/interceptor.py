import socket
import time
from datetime import datetime

class SimpleTCPServer:
    def __init__(self, host='0.0.0.0', port=9001):
        """
        Servidor TCP simple para recibir mensajes del escáner
        
        Args:
            host: Dirección IP a escuchar (0.0.0.0 = todas las interfaces)
            port: Puerto a escuchar (default: 9001)
        """
        self.host = host
        self.port = port
        self.socket = None
        self.connections_count = 0
        
    def start(self):
        """Inicia el servidor TCP"""
        try:
            # Crear socket TCP
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Permitir reutilización de la dirección
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Vincular socket al host y puerto
            self.socket.bind((self.host, self.port))
            
            # Escuchar conexiones (backlog de 5)
            self.socket.listen(5)
            
            print("=" * 70)
            print("SERVIDOR TCP - LABORATORIO DE REDES")
            print("=" * 70)
            print(f"[✓] Servidor iniciado correctamente")
            print(f"[✓] Escuchando en: {self.host}:{self.port}")
            print(f"[*] Esperando conexiones del escáner...")
            print(f"[*] Presione Ctrl+C para detener el servidor")
            print("=" * 70)
            print()
            
            # Bucle principal para aceptar conexiones
            while True:
                try:
                    # Aceptar conexión entrante
                    conn, addr = self.socket.accept()
                    self.connections_count += 1
                    
                    # Obtener timestamp
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    
                    print(f"[{timestamp}] Nueva conexión #{self.connections_count} desde {addr[0]}:{addr[1]}")
                    
                    # Recibir datos
                    data = conn.recv(1024)
                    
                    if data:
                        message = data.decode('utf-8')
                        print(f"           Mensaje recibido: '{message}'")
                        print(f"           Tamaño: {len(data)} bytes")
                    else:
                        print(f"           [!] Conexión cerrada sin datos")
                    
                    # Cerrar conexión
                    conn.close()
                    print()
                    
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"[!] Error al procesar conexión: {e}")
                    continue
                    
        except KeyboardInterrupt:
            print("\n" + "=" * 70)
            print("[!] Servidor detenido por el usuario")
            print(f"[*] Total de conexiones recibidas: {self.connections_count}")
            print("=" * 70)
        except Exception as e:
            print(f"\n[!] Error al iniciar el servidor: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Detiene el servidor y cierra el socket"""
        if self.socket:
            try:
                self.socket.close()
                print("[✓] Socket cerrado correctamente")
            except:
                pass

def main():
    """Función principal"""
    print("\n" + "=" * 70)
    print("CONFIGURACIÓN DEL SERVIDOR TCP")
    print("=" * 70)
    
    # Configuración del puerto
    try:
        port = int(input("Ingrese el puerto a escuchar (default: 9001): ").strip() or "9001")
    except ValueError:
        port = 9001
        print(f"Puerto inválido. Usando valor por defecto: {port}")
    
    # Crear e iniciar servidor
    server = SimpleTCPServer(port=port)
    
    print(f"\n[*] Presione Enter para iniciar el servidor...")
    input()
    
    server.start()

if __name__ == "__main__":
    main()
