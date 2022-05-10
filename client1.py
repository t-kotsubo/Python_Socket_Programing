import socket
import sys

from client0 import BUFSIZE


PORT = 50000
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("接続先サーバ: ")

try:
    client.connect((host, PORT))
except:
    print("接続できません")
    sys.exit()

msg = input("メッセージを入力： ")

client.sendall(msg.encode('UTF-8'))

data = client.recv(BUFSIZE)

print("サーバからのメッセージ")

print(data.decode('UTF-8'))

client.close()

