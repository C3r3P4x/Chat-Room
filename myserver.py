import socket
import threading
from os import path

clients_dict = {}
host = "127.0.0.1"
port = 55555
if path.exists('ChatLogs.txt'):
    pass
else:
    open("ChatLogs.txt", "w").close()
if path.exists('Clients.txt'):
    pass
else:
    open("Clients.txt", "w").close()
if path.exists('BannedClients.txt'):
    pass
else:
    open("BannedClients.txt", "w").close()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("Listening for connections...")


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message != b'':
                chat = f"{clients_dict[client]} : {message.decode("ascii")}"
                print(chat)
                broadcast(chat)
                write_log(chat)
                chat = b''
        except:
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        print(address)
        print("Connected with {}".format(str(address)))
        name = client.recv(1024).decode("ascii")
        ip = str(address).split(",")[0][2:-1]
        write_client(name, client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def write_client(name, connection):
    clients_dict[connection] = name
    exists = False
    file = open("Clients.txt", "r")
    for a in file.readlines():
        if a[:-1] == name:
            exists = True
            break
    file.close()
    if not exists:
        file = open("Clients.txt", "a")
        file.write(f"{name} : {connection}\n")
        file.close()


def broadcast(message):
    for people in clients_dict.keys():
        people.send(message.encode("ascii"))


def write_log(log):
    file = open("ChatLogs.txt", "a")
    file.write(f"{log}\n")
    file.close()


receive()
