#!/usr/bin/python

from socket import *
import sys

host = sys.argv[1]
port = int(sys.argv[2])
bufsize = 1024
addr = (host,port)

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.connect(addr)

while True:
    data = raw_input('please input: >>')
    if not data:
        break
    sockfd.send(data)

    data = sockfd.recv(bufsize)
    print data

sockfd.close()
