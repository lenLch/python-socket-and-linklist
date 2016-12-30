#!/usr/bin/python
from socket import *
from time import ctime
from select import *


host = '10.1.1.135'
port = 8888
bufsize = 1024
addr = (host,port)

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.bind(addr)
sockfd.listen(5)

inputs = [sockfd]

while True:
    rs,ws,es = select(inputs,[],[])
    for r in rs:
        if r is sockfd:
            connfd,addr = sockfd.accept()
            print('connected from:',addr)
            inputs.append(connfd)
        else:
            try:
                data = r.recv(bufsize)
                disconnect = not data
            except socket.error:
                disconnect = True
            if disconnect:
                print (r.getpeername(),'disconnected')
                inputs.remove(r)
                r.close()
            else:
                r.send(('[%s]: %s'%(ctime(),data)))

sockfd.close()
