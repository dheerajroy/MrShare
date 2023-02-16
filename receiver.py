import socket

class Receiver:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = self.addr = None
        self.connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        print('Waiting for connections...')
        self.connector.bind((self.host, self.port))
        self.connector.listen(1)
        self.conn, self.addr = self.connector.accept()

    def download(self, filename):
        with self.conn:
            print(f'connected by {self.addr}')
            data = b''
            print('Downloading...')
            while True:
                d = self.conn.recv(2048000)
                if d:
                    data += d
                else:
                    break
            with open(f"{filename}", 'wb') as f:
                f.write(data)
            print('File Downloaded Successfully!')
