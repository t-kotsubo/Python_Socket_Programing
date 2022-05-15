from socket import AF_INET, SOCK_STREAM, socket
import datetime


HOST = "localhost"
PORT = 50000
BUFSIZE = 4096

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

msg = client.recv(BUFSIZE)
print(msg.decode('UTF-8'))

client.close()




