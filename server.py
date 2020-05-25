import socket
from _thread import *

import pygame as pg

pg.init()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.gethostbyname(socket.gethostname())
port = 9090

try:
    sock.bind((server, port))
except socket.error as err:
    print(str(err))

sock.listen(2)
print("Aguardando uma conexão")

current_id = "0"
pos = ["0:32,400,30,400,r", "1:1248,400,1248,400,l"]
chat = ""
count = 0
zero_start = 0
one_start = 0
start_time = 0
flag = 0
just_end = 0


# Cada cliente trabalha em seu próprio encadeamento. Essa função cuida de receber e enviar de volta os dados
# necessários.
def connected_client(connection):
    global current_id, pos, chat, count, zero_start, one_start, start_time, flag, just_end

    connection.send(str.encode(current_id))
    current_id = "1"
    chat = "0:"
    reply = ""

    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")
            # print(reply)
            id = int(reply[0])

            if id == 1:
                if str(just_end) == str(0):
                    one_start = 1
                else:
                    just_end = 0
            elif id == 0:
                if str(just_end) == str(0):
                    zero_start = 1
                else:
                    just_end = 0

            if zero_start == 1 and one_start == 1 and flag == 0:
                count = 2
                start_time = pg.time.get_ticks()
                print("Start" + start_time / 1000)
                flag = 1

            if str(flag) == "1":
                time_left = 303 - (pg.time.get_ticks() - start_time) / 1000

                if int(time_left) <= 0:
                    count = 0
                    one_start = 0
                    zero_start = 0
                    flag = 0
                    just_end = 1

            arr = reply.split("?")
            pos[id] = str(id) + ":" + arr[1]
            reply = arr[0]

            if not data:
                connection.send(str.encode("Tchau"))
                break
            else:
                if len(reply) > 2:
                    print("Recebendo: " + reply)
                    chat = reply

                if len(reply) > 2:
                    print("Enviando: " + chat)

            connection.sendall(str.encode(chat + "?" + str(pos[0]) + "?" + str(pos[1]) + "?" + str(count)))

        except:
            break

    current_id = "0"
    pos = ["0:32,400,30,400,r", "1:1248,400,1248,400,l"]
    count = 0
    zero_start = 0
    one_start = 0
    flag = 0
    print("Conexão encerrada")
    connection.close()


while True:
    connection, address = sock.accept()
    print("Conectado a:", address)
    start_new_thread(connected_client, (connection,))
