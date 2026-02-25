import os
import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((input('HOST IP:'),55555))

DATA = ''
def recv():
    while True:
        data = client.recv(1024).decode()
        if data:
            DATA += '\n'+data
            os.run('cls')
            print(DATA)
thread = threading.Thread(target=recv)
thread.start()

while True:
    data = input()

    client.send(data.encode())
