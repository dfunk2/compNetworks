import socket

#create a socket
s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 #bind server to port so client can tell them apart
 #Ports are per-computer! 
s.bind(("localhost", 4395))

#server listens for client connection
s.listen()

while(True):
    #accept returns new sockets for specific connections
    #original socket is still there listening for more connections
    client_socket, client_addr = s.accept()
    print("client address ", client_addr)
    #send data to client
    client_socket.sendall("Data\n".encode())
    client_socket.close()


