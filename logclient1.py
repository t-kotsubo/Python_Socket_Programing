from socket import AF_INET, SOCK_STREAM, socket
import sys


HOST = "localhost"
PORT = 50000

client = socket(AF_INET, SOCK_STREAM)

try: 
    client.connect((HOST, PORT))
except:
    print("サーバーに接続できません。")
    sys.exit()

while True:
   msg = input("メッセージを入力：") 
   
   if msg == "q":
       break

   client.sendall(msg.encode('UTF-8')) 

client.close()
