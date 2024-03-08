from colorama import Fore

import socket
import threading
from os import path
import sys

if len(sys.argv) != 3:
    print("Usage: python client.py <server_ip> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])


clients_dict = {}


if not path.exists('ChatLogs.txt'):
    open("ChatLogs.txt", "w").close()

if not path.exists('Clients.txt'):
    open("Clients.txt", "w").close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()
color = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.WHITE, Fore.MAGENTA,
         Fore.CYAN, Fore.YELLOW, Fore.LIGHTRED_EX]

def handle(client):
    while True:
        try:
            he, message = clients_dict[client], client.recv(1024)
            msg = message.decode("ascii")
            write_log(f"{he} : {msg}")
            if message:
                chat = Fore.MAGENTA + f"{he} : " + color[len(clients_dict[client])%9] + f"{msg}"
                broadcast(chat, client)
        except ConnectionResetError:
            broadcast(Fore.RED + f"\n{clients_dict[client]} left the chat", client)
            del clients_dict[client]
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        name = client.recv(1024).decode("ascii")
        write_client(name, client)
        broadcast(Fore.GREEN + f"\n{clients_dict[client]} Joined the Chat", client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def write_client(name, connection):
    clients_dict[connection] = name
    exists = False
    with open("Clients.txt", "r") as file:
        for a in file.readlines():
            if a[:-1] == name:
                exists = True
                break
    if not exists:
        with open("Clients.txt", "a") as file:
            file.write(f"{name} : {connection}\n")


def broadcast(message, not_to):
    print(message)
    for people in clients_dict.keys():
        if people != not_to:
            try:
                people.send(message.encode("ascii"))
            except socket.timeout:
                print(Fore.RED + f"{people} left the chat")


def write_log(log):
    with open("ChatLogs.txt", "a") as file:
        file.write(f"{log}\n")


try:
    receive()
except KeyboardInterrupt:
    for a in clients_dict.keys():
        a.close()
    print("You pressed Ctrl + C, program closed")
    exit()
