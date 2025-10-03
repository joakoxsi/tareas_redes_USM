import socket, os

IP=""
PUERTO=""

socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketTCP.connect((IP,PUERTO))