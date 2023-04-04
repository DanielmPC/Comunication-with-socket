## Script para la comunicación entre dos computadoras con socket
## Server 

import socket 

HOST = "10.42.0.1"      # Direccion de loopback
PORT = 65123          # Debe ser mayor a 1023 (Puerto de escucha)

addr = (HOST, PORT)

"""
socket.socket(IP, TCP)
La IP es la versión de IP que vamos a usar (4 o 6)
El TCP es si vamos a usar una comunicación TCP o UDP

"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Asociamos el socket con la tarjeta de red

    s.bind(addr) #debe de ser una tupla
    s.listen()
    conn, address = s.accept() ## conn va a ser usado para enviar 
                               ## y recibir informacion
    with conn:
        print(f"conectado a {address}")
        while True: # Recibe los datos 
            data = conn.recv( 1024 )    # 1024 valor estandar

            print(data)

            if not data:
                break
            conn.sendall(data) 




