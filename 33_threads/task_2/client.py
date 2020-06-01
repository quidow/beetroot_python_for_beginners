import socket
import threading


class Client(threading.Thread):

    def __init__(self, host='localhost', port=5000):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = None

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.send(str.encode(data))
        data = bytes.decode(self.socket.recv(1024))
        print(data)

    def close(self):
        self.socket.close()
