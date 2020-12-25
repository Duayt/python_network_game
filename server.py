import socket
from _thread import start_new_thread
import sys

# IPv4 on local from ipconfig 192.168.1.113
server = "192.168.1.113"
port = 12345

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)  # listen to only 2
print("Waiting for a connection, Server Started")


def read_pos(txt):
    txt = txt.split(",")
    return int(txt[0]), int(txt[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


# for 2 players position
pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print(f"Recieved:{reply}")
                print(f"Sending: {reply}")

            conn.sendall(str.encode(make_pos(reply)))
        except:
            print("Something went wrong")
            break

    print("Lost connection")
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1