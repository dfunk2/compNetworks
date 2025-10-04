import socket
import sys
serverSocket = socket.socket()

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) > 1:
    Port = int(sys.argv[1])
else:
    Port = 28333
    
#leave address blank to default to local address
serverSocket.bind(('', Port))

serverSocket.listen()

while True:
    #new socket is created but original is still listen, accept returns a tuple
    new_conn = serverSocket.accept()
    print("Client IP address and Port", new_conn) #prints my IP address and port number
    #receive a new socket
    new_socket = new_conn[0]

    data = new_socket.recv(4096)
    clientRequest = data.decode("ISO-8859-1")
    print(clientRequest, end='')

    for i in enumerate(clientRequest):
        if clientRequest.endswith("\r\n\r\n"):
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\n"
            new_socket.sendall(response.encode("ISO-8859-1"))
            #close the new socket and continue by accepting a new socket
            new_socket.close()
    
