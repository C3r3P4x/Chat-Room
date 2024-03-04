import socket
import threading
from colorama import Fore
from os import path

admin_id = "admin"
admin_key = "admin"
clients_dict = {}
host = "127.0.0.1"
port = 9998

if not path.exists('ChatLogs.txt'):
    open("ChatLogs.txt", "w").close()

if not path.exists('Clients.txt'):
    open("Clients.txt", "w").close()

if not path.exists('BannedClients.txt'):
    open("BannedClients.txt", "w").close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(Fore.GREEN + "Listening for connections...")


def handle(client):
    while True:
        try:
            he, message = clients_dict[client], client.recv(1024)
            if clients_dict[client] == admin_id:
                admin(client, message)
                continue
            msg = message.decode("ascii")
            write_log(f"{he} : {msg}")
            if message:
                chat = Fore.MAGENTA + f"{he} : " + Fore.LIGHTBLUE_EX + f"{msg}"
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

        if name == admin_id:
            client.send("KEY".encode("ascii"))
            key = client.recv(1024).decode("ascii")
            if key == admin_key:
                client.send("Welcome to root dashboard\nAvailable functions: Kick or Ban\n".encode("ascii"))
                continue
            else:
                client.send("Invalid key".encode("ascii"))
                client.close()
                continue
        broadcast(Fore.GREEN + f"\n{clients_dict[client]} Joined the Chat", client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def admin(root, msg):
    while True:
        blocks = msg.split()
        if blocks[0] == "Kick" or "Ban":
            if len(blocks) == 2:
                if blocks[0] == "Kick":
                    if blocks[1] in clients_dict.values():
                        for sock, name in clients_dict.items():
                            if name == blocks[1]:
                                sock.send("You have been kicked out by the admin\n".encode("ascii"))
                                broadcast(f"{clients_dict[root]} kicked out {blocks[1]}", sock)
                                sock.close()
                                del clients_dict[sock]
                                msg = f"Admin kicked out {blocks[1]}"
                                broadcast(msg, root)
                                break
                    else:
                        root.send("Invalid username\n".encode("ascii"))
                elif blocks[0] == "Ban":
                    if blocks[1] in clients_dict.values():
                        for sock, name in clients_dict.items():
                            if name == blocks[1]:
                                broadcast("You have been banned by the admin\n")
                                sock.close()
                                del clients_dict[sock]
                                msg = f"Admin banned {blocks[1]}"
                                broadcast(msg, root)
                                with open("BannedClients.txt", "a") as banned_file:
                                    write_ban(blocks[1])
                                break
                    else:
                        root.send("Invalid username\n".encode("ascii"))
            else:
                root.send("Invalid command format. Please use 'Kick username' or 'Ban username'\n".encode("ascii"))
        else:
            broadcast(msg, root)


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


def write_ban(name):
    with open("BannedClients.txt", "a") as file:
        file.write(f"{name}\n")


try:
    receive()
except KeyboardInterrupt:
    for a in clients_dict.keys():
        a.close()
    print("You pressed Ctrl + C, program closed")
    exit()
