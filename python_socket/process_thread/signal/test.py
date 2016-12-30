#!/usr/bin/python
#coding=utf-8
#1.创建父子进程，父进程代表司机，子进程代表售票员
#2.当售票员捕捉到SIGINT时，发送SIGUSR1给司机，司机打印 let's gogogo
#  当售票员捕捉到SIGQUIT时，发送SIGUSR2给司机 司机说stop the bus
#  当司机捕捉到SIGSTP时，发送SIGUSR1给售票员 售票员说 get off the bus
#3. 当到达总站后，司机等待售票员下车（子进程退出） 然后自己下车（exit）

#os.kill(id,signaltype)就可以发送信号了

from signal import *
import os,time

pid = os.fork()

def receive_sig(signum,stack):#售票员接收的信号
    if signum == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    if signum == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    if signum  == SIGUSR1:
        print "get off the bus"
        exit()

def rec(signum,stack):#司机接收的信号
    if signum == SIGUSR1:
        print "let's go"
    if signum == SIGUSR2:
        print "stop the bus"
    if signum == SIGTSTP:
        os.kill(pid,SIGUSR1)
        os.wait()
        exit()

if pid < 0:
    print "create failed"
    exit()
elif pid == 0:
    print "child id",os.getpid()
    signal(SIGINT,receive_sig)
    signal(SIGQUIT,receive_sig)
    signal(SIGUSR1,receive_sig)
    signal(SIGTSTP,SIG_IGN)

else:
    print "parent id:",os.getpid()
    signal(SIGUSR1,rec)
    signal(SIGUSR2,rec)
    signal(SIGTSTP,rec)
    signal(SIGINT,SIG_IGN)
    signal(SIGQUIT,SIG_IGN)

while True:
    pass
