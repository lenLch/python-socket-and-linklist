#!/usr/bin/python
#coding=utf-8
from socket import *
import os,sys
print '''
        ----------command-------------
        ----------list----------------
        ----------get filename--------
        ----------put filaname--------
        ----------quit----------------
      '''


host = sys.argv[1]
port = int(sys.argv[2])
addr = (host,port)
bufsize = 10240

s = socket(AF_INET,SOCK_STREAM)
s.connect(addr)
while True:
    data = raw_input('please input command:>>')
    s.send(data)

    rec_data = s.recv(bufsize)
    if data.split(' ')[0] == 'list':
        print rec_data
        print 'list ok!'
    if data.split(' ')[0] == 'get':
        f_cp = open(data.split(' ')[1],'w')
        f_cp.write(rec_data)
        print data.split(' ')[0]+ " " +data.split(' ')[1]
        print "get %s ok!"%data.split(' ')[1]
    if data.split(' ')[0] == 'put':
        f_cp = open('/home/linux/Desktop/python_socket/tcp_socket/'+data.split(' ')[1],'w')
        f_cp.write(rec_data)
        print data.split(' ')[0]+ " " +data.split(' ')[1]
        print "put %s ok!"%data.split(' ')[1]
    if data.split(' ')[0] == 'quit':
        exit()






s.close()
