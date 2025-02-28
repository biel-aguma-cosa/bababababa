import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('10.12.156.183',55555))

def recv():
    while True:
        data = client.recv(1024).decode()
        if data:
            print(data)
thread = threading.Thread(target=recv)
thread.start()

while True:
    data = input()
    client.send(data.encode())