#!/usr/bin/python
#coding=utf-8


from socket import *
from time import sleep
import sys
import os

#客户端功能函数
class FtpClient(object):
    BUFSIZE = 1024
    def __init__(self,serveraddr):
        self.serveraddr = serveraddr

    def do_list(self):
        sockfd = socket()
        sockfd.connect(self.serveraddr)
        data = 'L'
        sockfd.send(data)
        
        data = sockfd.recv(self.BUFSIZE)

        if data[0:2] == 'OK':
            while True:
                data = sockfd.recv(self.BUFSIZE)
                if not data:
                    break
                print data
                sys.stdout.flush
        else:
            print "list error!"
            sockfd.close()
            return
        
        sockfd.close()
        print "list ok"
        return

    def do_get(self,filename):
        fd = open(filename,'wb')
        data = 'G '+filename
    
        sockfd = socket()
        sockfd.connect(self.serveraddr)
        sockfd.send(data)
        data = sockfd.recv(self.BUFSIZE)

        if data[0:2] == 'OK':
            while True:
                data = sockfd.recv(self.BUFSIZE)
                if not data:
                    break
                fd.write(data)
                fd.flush()
        else:
            print "get %s fail"%filename
            sockfd.close()
            fd.close
            return
        print "get %s OK"%filename
        sockfd.close()
        fd.close()
        return


    def do_put(self,filename):
        fd = open(filename,'rb')
        data = 'P '+filename
    
        sockfd = socket()
        sockfd.connect(self.serveraddr)
        sockfd.send(data)
        data = sockfd.recv(self.BUFSIZE)

        if data[0:2] == 'OK':
            while True:
                data = fd.readline()
                if not data:
                    break
                sockfd.send(data)
                sleep(0.01)
        else:
            print "put %s fail"%filename
            sockfd.close()
            fd.close
            return
        print "put %s OK"%filename
        sockfd.close()
        fd.close()
        return



#创建套接字等工作
def main():
    if len(sys.argv) < 3:
        print "Input valid arg"
        sys.exit(0)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    ftp = FtpClient(ADDR)

    while True:
        print "*********  command  ************"
        print "*********  list     ************"
        print "*********  get filename  *******"
        print "*********  put filename  *******"
        print "*********  quit     ************"
        print "Input command>>",

        data = raw_input()

        if data[0] == 'l':
            ftp.do_list()
        elif data[0] == 'g':
            ftp.do_get(data[4:])
        elif data[0] == 'p':
            ftp.do_put(data[4:])
        elif data[0] == 'q':
            sys.exit(0)
        else:
            print "The command error !!!"
            continue

if __name__ == '__main__':
    main()
