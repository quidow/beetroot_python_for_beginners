"""
Echo server with threading

Create a socket echo server which handles each connection in a separate Thread
"""

from echo_server import Server
from client import Client

if __name__ == "__main__":
    s = Server()
    s.start()
    c1 = Client()
    c1.start()
    c1.join()
    c1.send('test1')
    c2 = Client()
    c2.start()
    c2.join()
    c2.send('test2')
    c1.close()
    c2.close()
    s.close()
