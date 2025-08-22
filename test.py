import socket

mensaje = "Hola, mundo!xczxczxcjxixvhsñkglhvlkzfusdihvjkxlshdvkjxcvhkxvclkjxhcvkjxhvkxjhvlkzxvhklxvhlkxzvchklxvhkxvhckxljcvhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
largo_bytes = len(mensaje.encode('utf-8'))
print(f"El largo en bytes del mensaje es: {largo_bytes}")

host = "127.0.0.1"

# SERVICIO 1: Cliente TCP y Servidor TCP

port_tcp = 5006
puerto=5006

flag=True

# CLiente TCP mandando a Servidor TCP
cliente_tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente_tcp.connect((host,port_tcp))

cliente_tcp.sendall(mensaje.encode('utf-8'))
