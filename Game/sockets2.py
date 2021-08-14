import socketio

sio = socketio.Client()

# listeners will have 3 parameters
# self, sid, data

# emiters will have 2 parameters
# self, data


class SocketConnection(socketio.ClientNamespace):
    def on_connect(self):
        print("Connected to Server")
        self.emit("initialize_game", "player has connected", namespace="/game")

    # def on_move(self, sid, data):
    #     self.emit("from on move listener: ", data)

    def on_disconnect(self):
        print("Client has Disconnected")

    def move(self, the_move):
        print("the_move: ", the_move)
        self.emit("initialize_game", "player has connected", namespace="/game")


sio.register_namespace(SocketConnection("/game"))
sio.connect("http://localhost:8000")
sio.wait()
