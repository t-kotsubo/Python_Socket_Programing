import socket
import datetime


PORT = 50000

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

server.bind(('', PORT))

server.listen()

while True:

    client, addr = server.accept()
    msg = str(datetime.datetime.now())
    client.sendall(msg.encode('UTF-8'))
    print(msg, "接続要求有り")

    print(f'client: {client}')

    client.close()





