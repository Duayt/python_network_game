import socket
from _thread import start_new_thread
from player import Player
import pickle
from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv('IP_ADDRESS')
PORT = int(os.getenv('PORT'))

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    print(e)

s.listen(2)  # listen to only 2
print("Waiting for a connection, Server Started")


# for 2 players position
players = [Player(0, 0, 50, 50, (255, 0, 0)),
           Player(1000, 1000, 50, 50, (0, 0, 255))]

global global_break
global_break = False


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print(f"Recieved:{data}")
                print(f"Sending: {reply}")

            conn.sendall(pickle.dumps(reply))
        except:
            print("Something went wrong")
            break

    print("Lost connection")
    conn.close()
    global global_break
    global_break = True


current_player = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
    if global_break:
        break
