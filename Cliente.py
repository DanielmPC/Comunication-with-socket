# Cliente

import socket

HOST = "10.42.0.1"      ## IP DEL SERVER
PORT = 65123

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Hola mundo")    # Debemos de mandar los datos en binario

    data = s.recv(1024)

print("Recibido", repr(data))