import socket
import threading
from os import path
import sys
from colorama import Fore

clients_dict = {}
exit_event = threading.Event()


def handle(client):
    while True:
        try:
            name, message = clients_dict[client], client.recv(1024).decode("ascii")

            write_log(f"{name}: {message}")

            broadcast(f"{name}: {message}", client)
        except ConnectionResetError:
            # Handle client disconnect
            handle_disconnect(client)
            break


def handle_disconnect(client):
    if client in clients_dict:
        name = clients_dict[client]
        del clients_dict[client]
        client.close()
        broadcast(Fore.RED + f"\n{name} left the chat", client)


def receive():
    while not exit_event.is_set():
        try:
            client, address = server.accept()
            name = client.recv(1024).decode("ascii")
            clients_dict[client] = name
            write_client(name, client)
            broadcast(Fore.GREEN + f"\n{name} joined the chat", client)
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except socket.error as e:
            print(f"Error accepting client connection: {e}")


def broadcast(message, not_to):
    print(message)
    for client_socket in clients_dict.keys():
        if client_socket != not_to:
            try:
                client_socket.send(message.encode("ascii"))
            except socket.error as e:
                print(f"Error broadcasting message to client: {e}")
                handle_disconnect(client_socket)


def write_client(name, connection):
    exists = False
    with open("Clients.txt", "r") as file:
        for line in file.readlines():
            if line.strip() == name:
                exists = True
                break
    if not exists:
        with open("Clients.txt", "a") as file:
            file.write(f"{name}\n")


def write_log(log):
    with open("ChatLogs.txt", "a") as file:
        file.write(f"{log}\n")


if __name__ == "__main__":
    if not path.exists('ChatLogs.txt'):
        open("ChatLogs.txt", "w").close()

    if not path.exists('Clients.txt'):
        open("Clients.txt", "w").close()
    if len(sys.argv) != 3:
        print("Usage: python server.py <server_ip> <port>")
        sys.exit(1)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))

    server.listen()

    print(Fore.GREEN + "Server Established\n")

    try:
        receive()
    except KeyboardInterrupt:
        for client_socket in clients_dict.keys():
            client_socket.close()
        server.close()
        print("You pressed Ctrl + C, program closed")
        sys.exit()
