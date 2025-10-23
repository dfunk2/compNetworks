import socket
import os
#map file extension to MIME type
fileExt_MIME = {
    ".txt": "text/plain",
    ".html": "text/html"
}

#create a socket
webServer = socket.socket()
webServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

webServer.bind(('', 28333))
webServer.listen()

while True:
    #accept connections
    newConnection = webServer.accept()
    newSocket = newConnection[0]
    
    try: 
        data = newSocket.recv(4096)
        browserRequest = data.decode("ISO-8859-1")

        if("\r\n\r\n" in browserRequest):
            #parse the request header from client to get file name and file extension
            parsedData = browserRequest.split("\r\n")
            getLine = parsedData[0]

            parts = getLine.split(' ')
            method, pathVar, protocol = parts

            fileName = os.path.split(pathVar)

            fileExt = os.path.splitext(fileName[1])

        #build an http response packet w/file data in payload
        if(fileExt[1] not in fileExt_MIME): 
            raise Exception("File extension not supported")
        
        contentType = fileExt_MIME[fileExt[1]]
  
        with open(fileName[1], "rb") as fp:
            payloadData = fp.read()
            contentLength = len(payloadData)

        #send the HTTP response back to the client
        responseHeaders = (
            f"HTTP/1.1 200 OK\r\n"
            f"Content-Type: {contentType}\r\n"
            f"Content-Length: {contentLength}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
        )
        newSocket.sendall(responseHeaders.encode("ISO-8859-1"))
        newSocket.sendall(payloadData)
            
    except:
        error = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 13\r\n"
            "Connection: close\r\n"
            "\r\n"
            "404 not found\r\n\r\n"
        )
        newSocket.sendall(error.encode("ISO-8859-1"))
        newSocket.close()
    finally:
         newSocket.close()

       

