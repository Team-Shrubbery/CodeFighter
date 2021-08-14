import socketio

# sio = socketio.Client


class SocketConnection:
    sio = socketio.Client
    sio.connect("http://localhost:8000")

    def __init__(self):
        pass

    @sio.event(namespace="/game")
    def connect(self):
        print("connection established")
        nonlocal sio
        sio.emit("from client", "will this work?")

    @sio.event(namespace="/game")
    def move(self, data):
        sio.emit("move", "move was triggered")

    @sio.event(namespace="/game")
    def disconnect(self):
        print("disconnected from server")
