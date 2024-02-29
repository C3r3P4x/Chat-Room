import socket
import threading
from os import path

host = "127.0.0.1"
port = 55551
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
                print(f"{client} : {message.decode("ascii")}")
        except:
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        client.send("Enter your name : ".encode("ascii"))
        name = client.recv(1024).decode("ascii")
        clients = open("Clients.txt","a")
        clients.write(name + "\n")
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
