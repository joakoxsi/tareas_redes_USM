import socket

host="127.0.0.1"
puerto= 5005

servidor=  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind((host,puerto))

while True:
    data, addr =servidor.recvfrom(1024)
    print(data)