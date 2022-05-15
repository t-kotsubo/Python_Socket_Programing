from asyncio.windows_utils import BUFSIZE
import socket
import datetime


PORT = 50000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('', PORT))

while True:
    data, toClient = server.recvfrom(BUFSIZE)
    msg = str(datetime.datetime.now())

    server.sendto(msg.encode('UTF-8'), toClient)
    
    print('接続要求あり')
    print('クライアント:', toClient)

    