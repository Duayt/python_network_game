import socket
import pickle
from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv('IP_ADDRESS')
PORT = int(os.getenv('PORT'))


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


# n = Network()
# print(n.send("hello"))
# print(n.send("bye"))
