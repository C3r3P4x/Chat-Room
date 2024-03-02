import socket
import threading

host = "127.0.0.1"
port = 9998
name = input("Enter your name : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except:
    print("\nError 404!, Server not found :(")
    quit()

client.send(name.encode("ascii"))


def write():
    while True:
        message = input().encode("ascii")
        try:
            client.send(message)
        except:
            print("\nError 404!, Server not found :(")
            break


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "KEY":
                key = input("Enter Password : ")
                client.send(key.encode("ascii"))
                print(client.recv(1024).decode("ascii"))
            elif message:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
