import socket
from caesar import encrypt

host = 'localhost'
port = 5000
addr = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    udp_socket.bind(addr)
    while True:
        print('wait data...')
        conn, addr = udp_socket.recvfrom(1024)
        print(f'client addr: {addr}, client data: {conn}')
        data = str.encode(encrypt(bytes.decode(conn), 7))
        udp_socket.sendto(data, addr)
