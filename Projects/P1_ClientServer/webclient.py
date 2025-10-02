'''In this program I am creating a socket program that can download files from a web server, a web client. 
I will also write a program to handle the request from the web client, a web server.'''

import socket

#create socket and server
clientSocket = socket.socket()
server = (("google.com", 80))

#connect socket to server
clientSocket.connect(server)
    
#HTTP request
request = "GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n"

#Send HTTP request
clientSocket.sendall(request.encode("ISO-8859-1"))

#receive the web response
data = clientSocket.recv(4096)
string = data.decode("ISO-8859-1")
for char in string:
    print(char, end='')

clientSocket.close()
        

