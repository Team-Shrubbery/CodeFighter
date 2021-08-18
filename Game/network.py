import socket
import pickle

# section 5 starts at 1:03


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        # self.SERVER = "45.56.74.237"
        self.PORT = 5555
        self.ADDR = (self.SERVER, self.PORT)
        # this will make the connection when Network gets Instantiated
        # player will then return and become Player Instance
        self.player = self.connect()

    def getPlayer(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            # the byta data received from server needs to get converted back to object
            # pickle load will change byte data into object
            # this is returning the Player Instance
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            # when you send to server, need to encode & serialize
            # turns data obj into a pickle serialized object
            self.client.send(pickle.dumps(data))
            # loads byte data back into object
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)
