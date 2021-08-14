import socketio

sio = socketio.Client()

# listeners will have 3 parameters
# self, sid, data

# emiters will have 2 parameters
# self, data


class SocketConnection(socketio.ClientNamespace):
    # def __init__(self):
    #     pass

    def on_connect(self):
        print("We Connected")

    def on_position(self, data):
        print("We are: ", data)
        # self.player = data
        # print("self.player: ", self.player)

    # def on_move(data):
    #     print("Player 1 Received Move: ", data)

    def on_receive(self, data):
        print("We got this from other player: ", data)

    @staticmethod
    def sendmove(data):
        print("Send Move to Server: ", data)
        sio.emit("move", data)

    def on_disconnect(self):
        print("We Disconnected from server")


sio.register_namespace(SocketConnection("/"))
sio.connect("http://localhost:8000")
# sio.wait()
