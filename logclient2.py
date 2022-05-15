from socket import AF_INET, SOCK_STREAM, socket
import sys

HOST = "localhost"
PORT = 50000
DATAFILE = "data.txt"

client = socket(AF_INET, SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except:
    print("サーバに接続できません。")    
    sys.exit()

file = open(DATAFILE, "rt", encoding='UTF-8')
msg = file.read()

client.sendall(msg.encode('UTF-8'))

client.close()





    


