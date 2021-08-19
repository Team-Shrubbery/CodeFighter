import socketio


class SocketConnection:

    global sio
    global opponent_move
    global position1
    global position2
    global direction1
    global direction2
    global character1
    global character2

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
        global position1
        global position2
        global direction1
        global direction2
        global character1
        global character2
        if data == "Player1":
            position1 = 100
            direction1 = "RIGHT"
            character1 = "Alucard"
            position2 = 660
            direction2 = "LEFT"
            character2 = "Fixer"
        else:
            position1 = 660
            direction1 = "LEFT"
            character1 = "Fixer"
            position2 = 100
            direction2 = "RIGHT"
            character2 = "Alucard"

    def get_player1_x(self):
        return position1

    def get_player1_direction(self):
        return direction1

    def get_player2_x(self):
        return position2

    def get_player2_direction(self):
        return direction2

    def get_player1_character(self):
        return character1

    def get_player2_character(self):
        return character2

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
        sio.connect("http://localhost:8000")
