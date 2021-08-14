import socketio

sio = socketio.Client()

# listeners will have 3 parameters
# self, sid, data

# emiters will have 2 parameters
# self, data


class SocketConnection(socketio.ClientNamespace):
    def on_connect(self):
        print("Player 1 Connected")
        sio.emit("message", "Player 1")

    # def on_move(self, sid, data):
    #     self.emit("from on move listener: ", data)
    def on_move(data):
        print("Player 1 Received Move: ", data)

    @staticmethod
    def sendmove(data):
        print("This is what were trying to send", data)
        sio.emit("move", data)

    def on_disconnect(self):
        print("Player 1 Disconnected from server")


sio.register_namespace(SocketConnection("/"))
sio.connect("http://localhost:8000")
# sio.wait()
