import socket
import threading
from os import path
from colorama import Fore

clients_dict = {}
host = "127.0.0.1"
port = 9998
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
print(Fore.GREEN + "Listening for connections...")


def handle(client):
    while True:
        try:
            he, message = clients_dict[client], client.recv(1024)
            msg = message.decode("ascii")
            write_log(f"{he} : {msg}")
            if message:
                chat = Fore.BLUE + f"{he} : " + Fore.RED + f"{msg}"
                broadcast(chat, client)
        except:
            broadcast(Fore.RED + f"\n{clients_dict[client]} left the chat", client)
            del clients_dict[client]
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        name = client.recv(1024).decode("ascii")
        if name == "admin":
            client.send("KEY".encode("ascii"))
            key = client.recv(1024)
            if key == "admin":
                client.send("Log in successful".encode("ascii"))
        write_client(name, client)
        broadcast(Fore.GREEN + f"\n{clients_dict[client]} Joined the Chat", client)
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


def broadcast(message, not_to):
    print(message)
    for people in clients_dict.keys():
        if people != not_to:
            try:
                people.send(message.encode("ascii"))
            except socket.timeout:
                print(Fore.RED + f"{people} left the chat")


def write_log(log):
    file = open("ChatLogs.txt", "a")
    file.write(f"{log}\n")
    file.close()


receive()
