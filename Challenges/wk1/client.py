import socket

client = socket.socket()
server = (('localhost', 1026))
#client is assigned to and bound to a port

client.connect(server)

""" data = client.recv(256)
#decode bytes to string
str = data.decode()
for char in str:
    print(char, end='') """
