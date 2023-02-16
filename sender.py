import socket

class Sender:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):  
        self.connector.connect((self.host, self.port))

    def send(self, filename):
        with open(f'{filename}', 'rb') as f:
            self.connector.sendall(f.read())
        print('Sent')
