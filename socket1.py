#python socket program to access a HTML webpage using HTTP

import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('www.py4inf.com', 80))
mySocket.send(('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n').encode())

while True:
    data = mySocket.recv(512).decode()
    if ( len(data) < 1 ) :
        break
    print("%s" % data)
mySocket.close()
