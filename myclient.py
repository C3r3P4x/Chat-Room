import socket
import threading
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1', 55555))
except:
    print("Error 404!, Server not found :(")
    quit()
name = input("Enter your name : ")
client.send(name.encode("ascii"))


def write():
    while True:
        try:
            client.send(input().encode("ascii"))
        except:
            print("Error 404!, Server not found :(")
            break


def receive():
    while True:
        try:

            message = client.recv(1024).decode('ascii')
            client.send(name.encode('ascii'))
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
