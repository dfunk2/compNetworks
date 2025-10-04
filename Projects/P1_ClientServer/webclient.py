'''In this program I am creating a socket program that can download files from a web server, a web client. 
I will also write a program to handle the request from the web client, a web server.'''

import socket
import sys

#create socket and server
clientSocket = socket.socket()

#specify a IP in the command line
Host = sys.argv[1] 
#default to port 80 unless specified in command line
if len(sys.argv) > 2:
    Port = int(sys.argv[2])
else:
    Port = 80
server = (Host, Port)

#connect socket to server
clientSocket.connect(server)
    
#HTTP request
request = f"GET / HTTP/1.1\r\nHost: {Host}\r\nConnection: close\r\n\r\n"

#Send HTTP request
clientSocket.sendall(request.encode("ISO-8859-1"))

#receive the web response
while True:
    data = clientSocket.recv(4096)
    str = data.decode("ISO-8859-1")
    print(str, end='')
    #server stop sending data
    if len(str) == 0:
        break
clientSocket.close()
        

