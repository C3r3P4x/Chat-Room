import socket
import threading
from colorama import Fore
import sys

if len(sys.argv) != 3:
    print("Usage: python server.py <server_ip> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
print(
    Fore.GREEN + "use alphabets, letters and underscores only " + Fore.RED + " (max length 14) \n" + Fore.RESET + "Enter your name: ")
while True:
    name = input()
    count = 0
    for char in name:
        if char.isdigit() or char.isalpha() or char == "_":
            count += 1
    if count == len(name):
        print(Fore.LIGHTBLUE_EX + f"welcome, {name}")
        break
    else:
        print("Invalid name, try again\nEnter your name : ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except ConnectionRefusedError:
    print(Fore.RED + "\nError 404! Server not found :(")
    quit()

client.send(name.encode("ascii"))


def write():
    while True:
        message = input().encode("ascii")
        if message == "exit":
            exit()
        try:
            client.send(message)
        except ConnectionResetError:
            print("\nConnection lost with the server.")
            break


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except ConnectionResetError:
            print("Connection lost with the server.")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
