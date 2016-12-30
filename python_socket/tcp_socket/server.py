#!/usr/bin/python
#coding=utf-8
from socket import *
import sys,os


#显示文件清单
def list():
    for i in os.listdir('/home/linux/Desktop/python_socket/tcp_socket/'):
        if os.path.isfile('/home/linux/Desktop/python_socket/tcp_socket/'+i):
            connfd.send(i+'\n')

#下载文件
def getfile(name):
    for i in os.listdir('/home/linux/Desktop/python_socket/tcp_socket/'):
        if os.path.isfile('/home/linux/Desktop/python_socket/tcp_socket/'+i):
            if i == name:
                f = open(i,'r')
                s = f.read()
                connfd.send(s)

def putfile(name):
    f = open(name,'r')
    s = f.read()
    connfd.send(s)

def quit():
    exit()

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    addr = (host,port)
    bufsize = 10240

    s = socket(AF_INET,SOCK_STREAM)

    s.bind(addr)
    s.listen(5)

    while True:
        print "waiting for connection...."
        connfd,addr = s.accept()
        print 'connected from: ',addr

        while True:
            data = connfd.recv(bufsize)
            if data.split(' ')[0] == 'list':
                list()
            if data.split(' ')[0] == 'get':
                getfile(data.split(' ')[1])
            if data.split(' ')[0] == 'put':
                putfile(data.split(' ')[1])
            if data.split(' ')[0] == 'quit':
                quit()


    connfd.close()
    s.close()
