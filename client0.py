from asyncio.windows_utils import BUFSIZE
from ctypes.wintypes import POINT
# from socket import socket
import socket

HOST = "localhost" # 接続先ホストの名前
PORT = 50000
BUFSIZE = 4096

# ソケットの作成
# 第1引数　IPv4の場合：AF_INET, IPv6の場合：socket.AF_INET6
# 第2引数　TCPの場合：SOCK_STREAM、UDPの場合：DATA_DGRAM
# 第3引数以降はTCP、UDPの通信では省略する
          
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4、TCPで接続する場合, 
# 参照：https://docs.python.org/ja/3/library/socket.html#socket.AF_INET

# サーバとの接続
client.connect((HOST, PORT))
# サーバからのメッセージの受診
data = client.recv(BUFSIZE)
# recv()で受診したデータはbytesオブジェクトとして扱うためUTF-8にデコードする
print(data.decode("UTF-8"))
# コネクションのクローズ
client.close()


