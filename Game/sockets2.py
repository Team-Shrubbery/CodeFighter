from signal import SIGIO
import socketio


class SocketConnection:

    global sio
    global opponent_move
    global position

    sio = socketio.Client()

    def __init__(self):
        pass

    @sio.event
    def connect():
        print("We Connected")

    def get_position(self):
        return position

    def get_opponent_move(self):
        global opponent_move
        try:
            return opponent_move
        except NameError:
            return None

    @sio.event
    def position(data):
        print("We are: ", data)
        global position
        position = data

    @sio.event
    def receive(data):
        print("We got this from other player: ", data)
        global opponent_move
        opponent_move = data

    @staticmethod
    def sendmove(data):
        print("Send Move to Server: ", data)
        sio.emit("move", data)

    @sio.event
    def disconnect():
        print("We Disconnected from server")

    @staticmethod
    def start_connection():
        print("we got to start connection")
        sio.connect("http://localhost:8000")
