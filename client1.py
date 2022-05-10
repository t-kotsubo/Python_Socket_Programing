from asyncio.windows_utils import BUFSIZE
from http import client
from pydoc import cli
import socket
import sys

from bleach import clean

HOST = "localhost"
PORT = 50000
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("接続先サーバ：")

try:
    client.connect(( HOST, PORT ))
except:
    print("接続できません。")
    
msg = input("メッセージを入力：")

client.send(msg.encode("UTF-8"))

data = client.recv(BUFSIZE)
print("サーバからのメッセージ")
print(data.decode("UTF-8"))

clean.close()
