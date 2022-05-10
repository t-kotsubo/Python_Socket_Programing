from asyncio.windows_utils import BUFSIZE
from http import client
from math import ceil
import socket


HOST = 'localhost' # もしくはIPv6のループバックアドレス "::1"
PORT = 50000
BUFSIZE = 4096

# ソケットの作成
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# サーバとの接続
client.connect((HOST, PORT))

# サーバからメッセージの受信
data =  client.recv(BUFSIZE)

print(data.decode('UTF-8'))

# コネクションのクローズ
socket.close()