import socket

host = 'localhost'
port = 5000
addr = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    data = str.encode(input('write to server: '))
    udp_socket.sendto(data, addr)
    conn, addr = udp_socket.recvfrom(1024)
    data = bytes.decode(conn)
    print(data)
