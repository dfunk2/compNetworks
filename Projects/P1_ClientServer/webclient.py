'''In this program I am creating a socket program that can download files from a web server, a web client. 
I will also write a program to handle the request from the web client, a web server.'''

import socket

def webclient():
    s = "hello world!"
    b = s.encode("ISO-8859-1")
    #create socket
    socket.socket()
    #connect socket to destination
    b.connect("example.com", 80)
    GET / HTTP/1.1
    Host: example.comee
    Connection: close
    b.sendall()
    d = b.recv(4096)
    if len(d) == 0:
        print("all done!")
    b.close()

webclient()