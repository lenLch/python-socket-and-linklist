#!/usr/bin/python
from socket import *
from select import *

s = socket()
host = '10.1.1.135'
port = 8888

s.bind((host,port))

fdmap = {s.fileno():s}

s.listen(5)

p = poll()
p.register(s)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = s.accept()
            print "get connection from :",addr
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print fdmap[fd].getpeername(),'disconnected'
                p.unregister(fd)
                del fdmap[fd]
            else:
                print data
                c.send('receive message')

s.close()
