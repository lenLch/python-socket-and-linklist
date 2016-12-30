#!/usr/bin/python
from socket import *

host = '10.1.1.135'
port = 8888
addr = (host,port)
bufsize = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input(">>>>")

    n = sockfd.sendto(data,addr)
    print n

    data,ADDR = sockfd.recvfrom(bufsize)
    print data

sockfd.close()
