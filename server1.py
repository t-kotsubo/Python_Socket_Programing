import socket
import datetime


PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(( '', PORT ))

server.listen()

while True:
    toClient, addr = server.accept()    
    msg = str(datetime.datetime.now())
    toClient.sendall(msg.encode('UTF-8'))
    print(msg, "接続要求あり") 
    print(toClient)
    toClient.close()

    
    

    

