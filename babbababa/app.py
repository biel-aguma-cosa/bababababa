import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('10.12.156.183',55555))

print(f'HOST NAME: {socket.gethostname()}')

clients = []
client_data = {}
all_data = []
def broadcast(data):
    if clients != []:
        for client in clients:
            client.send(data.encode())
        print('[data broadcasted]')
def loop(sock,addr):
    while True:
        try:
            rdata = sock.recv(1024).decode()
            if '%$setname:' == rdata[:10]:
                client_data[str(addr)] = rdata[10:]
                print('[name set]')
            if str(addr) in client_data:
                data = f'[{client_data[str(addr)]}]:{rdata}'
            else:
                data = f'[{addr}]:{rdata}'
            all_data.append(data)
            print(f'[data received]: {data}')
            broadcast(data)
        except:
            if str(addr) in client_data:
                data = f'[{client_data[str(addr)]} desconectou-se]'
            else:
                data = f'[{addr} desconectou-se]'
            clients.remove(sock)
            break
def connection():
    global clients
    while True:
        sock, addr = server.accept()
        print(f'[{addr[0]}:{addr[1]} connected]')
        if sock not in clients: clients.append(sock)
        if all_data != []:
            package = ''
            for data in all_data[:]:
                package += (data + '\n')
            sock.send(package.encode())
        thread = threading.Thread(target=loop,args=(sock,addr))
        thread.start()

server.listen(5)
connection()