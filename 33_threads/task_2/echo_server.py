import socket
import threading


class Server(threading.Thread):

    def __init__(self, host='localhost', port=5000, conn_number=5):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.conn_number = conn_number
        self.server = None
        self.runserver = True
        self.clients = []

    def open_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(self.conn_number)

    def run(self):
        self.open_socket()

        while True:
            if not self.runserver:
                break
            try:
                conn, addr = self.server.accept()
            except:
                break
            client = ClientThread(conn, addr)
            client.start()
            self.clients.append(client)

    def close(self):
        for c in self.clients:
            c.close()
        self.server.close()
        self.runserver = False


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.size = 1024
        self.runclient = True

    def run(self):
        print('connected:', self.addr)
        while True:
            if not self.runclient:
                break
            data = self.conn.recv(self.size)
            self.conn.send(data.upper())
        self.conn.close()

    def close(self):
        self.runclient = False
