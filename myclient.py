import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55551))
name = input("Enter your name : ")


def write():
    while True:
        client.send(input().encode("ascii"))
        pass

def receive():
    while True:
        try:

            message = client.recv(1024).decode('ascii')
            if message == "Enter your name : ":
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
