import socket 

#create a socket
s = socket.socket()

#connect the socket to a server
server = ('time.nist.gov', 13)
#connect socket to server
s.connect(server)

#receive data, the amount of data can be customized but you want to input a large chunk to cover your bases
data = s.recv(256)

#decode bytes to string
str = data.decode()
for char in str:
    print(char, end='')