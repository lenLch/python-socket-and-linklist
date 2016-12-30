#!/usr/bin/python
from socket import *

host = '10.1.1.135'
port = 8888
addr = (host,port)
bufsize = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.bind(addr)

while True:
    print "waiting for message...."
    data,addr = sockfd.recvfrom(bufsize)
    print 'client addr: ',addr
    sockfd.sendto('hello\n',addr)

sockfd.close()
