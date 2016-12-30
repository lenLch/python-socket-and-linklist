#!/usr/bin/python
import socket
from time import sleep

host = '10.1.1.135'
port = 8889
addr = (host,port)
bufsize = 1024

sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockfd.bind(addr)

sockfd.listen(5)

while True:
    print "waiting connection....."
    sockfd.setblocking(1)
    connfd,addr = sockfd.accept()
    print 'connected from: ',addr

    while True:
        data = connfd.recv(bufsize)
        if data == '\r\n':
            break
        print data
        connfd.send('hello\n')
    time.sleep(1)
    print "++++++++"

connfd.close()
sockfd.close()
