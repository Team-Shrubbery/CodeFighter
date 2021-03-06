import socketio


class SocketConnection:

    global sio
    global opponent_move
    global character

    sio = socketio.Client()

    def __init__(self):
        pass

    @sio.event
    def connect():
        print("We Connected")

    def get_opponent_move(self):
        global opponent_move
        try:
            return opponent_move
        except NameError:
            return None

    def reset_opponent_move(self):
        global opponent_move
        opponent_move = None

    @sio.event
    def position(data):
        print("We are: ", data)
        global character
        if data == "Player1":
            character = "Alucard"
        elif data == "Player2":
            character = "Fixer"

    def get_our_character(self):
        return character

    @sio.event
    def receive(data):
        # print("We got this from other player: ", data)
        global opponent_move
        opponent_move = data

    @staticmethod
    def sendmove(data):
        # print("Send Move to Server: ", data)
        sio.emit("move", data)

    @sio.event
    def disconnect():
        print("We Disconnected from server")

    @staticmethod
    def start_connection():
        # print("we got to start connection")
        # sio.connect("http://localhost:8000")
        sio.connect("https://codefighter-server.herokuapp.com")
