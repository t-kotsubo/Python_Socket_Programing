from asyncio.windows_utils import BUFSIZE
import socket
import datetime


PORT = 50000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('', PORT))

server.listen()

while True:
    toClient, addr = server.accept()
    msg = str(datetime.datetime.now())
    print(msg, '接続要求あり')
    print('クライアント：', toClient)
    
    data = toClient.recv(BUFSIZE)
    print('data:', data.decode('UTF-8'))
    
    toClient.sendall(msg.encode('UTF-8'))
    toClient.close()