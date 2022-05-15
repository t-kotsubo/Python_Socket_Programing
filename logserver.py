from asyncio.windows_utils import BUFSIZE
from socket import AF_INET, SOCK_STREAM, socket
import datetime


PORT = 50000
BUFSIZE = 4096

server = socket(AF_INET, SOCK_STREAM)

server.bind(("", PORT))

server.listen()

while True:
    client, addr = server.accept()

    d = datetime.datetime.now()
    
    fname = d.strftime("%Y%m%d%H%M%S%f")

    print(fname, "：接続要求有り")
    print(client)

    fout = open(fname + ".txt", "wt")
    
    try:
        while True:
            data = client.recv(BUFSIZE)
            if not data:
                break
            print(data.decode('UTF-8'))
            print(data.decode('UTF-8'), file=fout) # ファイルに出力する
            # (参考) https://qiita.com/pytry3g/items/aa38d8c2acf59b90aaac
    except:
        print("エラーが発生しました(接続終了)")
    
    client.close()
    fout.close()