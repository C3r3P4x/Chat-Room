import socket
import threading
from colorama import Fore
import sys

if len(sys.argv) != 3:
    print("Usage: python server.py <server_ip> <port>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

exit_event = threading.Event()

print(
    Fore.GREEN + "Use alphabets, letters, and underscores only " + Fore.RED + "(max length 14)\n" + Fore.RESET + "Enter your name: ")
try:

    while True:
        name = input()
        count = 0
        for char in name:
            if char.isdigit() or char.isalpha() or char == "_":
                count += 1
        if count == len(name):
            print(Fore.LIGHTBLUE_EX + f"Welcome, {name}")
            break
        else:
            print("Invalid name, try again\nEnter your name: ")
except KeyboardInterrupt:
    quit()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except ConnectionRefusedError:
    print(Fore.RED + "\nError 404! Server not found :(")
    exit_event.set()
    quit()
try:
    client.send(name.encode("ascii"))
except ConnectionResetError:
    print("\nConnection lost with the server.")
    exit_event.set()
    client.close()
    exit()


def write():
    while True:
        message = input().encode("ascii")
        if message.decode("ascii") == "exit":
            client.close()
            exit_event.set()
            sys.exit()
        try:
            client.send(message)
        except ConnectionResetError:
            print("\nConnection lost with the server.")
            break


def receive():
    while not exit_event.is_set():
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except ConnectionResetError:
            print("Connection lost with the server.")
            break
        except ConnectionAbortedError:
            print("Connection aborted...")
            break


try:
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
except KeyboardInterrupt:
    print("Closing the program")
    exit_event.set()
    client.close()
    exit()
