""" ※このプログラムはunix系OSのみで稼働する(Windows不可) """

from socket import AF_INET, SOCK_STREAM, socket
import sys
import os
import time


PORT = 50000
SLEEPTIME = 10


if os.name != 'posix':
    print('本プログラムは、unix系OS以外では稼働しません。')
    sys.exit()

# 接続先の設定
host = input("接続先サーバ：")

while True:
    client = socket(AF_INET, SOCK_STREAM)
    
    try:
        client.connect(('', PORT))
    except:
        print('サーバに接続できません。')
        sys.exit()
    
    loadavg = os.getloadavg()    
    print('loadavg:', loadavg )
    
    client.sendall(str(loadavg).encode('UTF-8'))
    
    client.close()
    
    time.sleep(SLEEPTIME)