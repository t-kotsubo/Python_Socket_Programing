import socket
import datetime
import threading 


PORT = 50000
BUFSIZE = 4096

def client_handler(client, client_no, msg):
    """クライアントとの接続処理メソッド"""

    data = client.recv(BUFSIZE)
    print(f'({client_no}) {data.encode("UTF-8")}')

    client.sendall(msg.encode("UTF-8"))
    client.close()

server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", PORT))

server.listen()

# クライアントの受付番号の初期化
client_no = 0

while True:
    client, addr = server.accept()
    client_no += 1

    msg = str(datetime.datetime.now())

    print(f'接続要求有り({client_no})')
    print(client)
    # スレッドの設定と起動
    p = threading.Thread(target=client_handler, args=(client, client_no, msg))

    p.start()