import socket

# ポートの設定
PORT = 50000

# socketの生成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# アドレスとポートの設定
server.bind('', PORT)

# 待機状態にする
server.listen()

# 送信先のソケットを取得する
client, addr = server.accept()

# データを送信する
client.sendall(b"Hi, nice to meet you!\n")

# 接続を解除する
client.close()
server.close()


