#!/usr/bin/python
#coding=utf-8

from signal import *
from time import sleep

#信号处理

#1. 忽略信号
#2. 采用默认方式处理  默认处理方式： 终止进程，暂停进程，忽略
#3. 采用指定函数处理

alarm(7)

# signal(SIGALRM,SIG_DFL) #采用默认的方式处理
signal(SIGINT,SIG_IGN) #忽略信号

while True:
    pass
