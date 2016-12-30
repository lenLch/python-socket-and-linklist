#!/usr/bin/python
#coding=utf-8
import os
from signal import *
pid = os.fork()
#这个程序实际上是两个进程，子进程继承了父进程的所有代码，但是子进程是从第五行的赋值开始
#执行的，还有，他虽然不执行上面的代码，但是他会承受父进程执行所有的结果。
#其实这两个进程是同时进行的，但是在内核调用的时候，父进程先执行的概率唯99.7%。内核有这样的一个机制。
if pid < 0:
    print "create process failed"
elif pid == 0:
    print "this is child process",os.getpid()
    print os.getppid()
    exit()
else:
    # os.wait()
    # print os.waitpid(-1,os.WNOHANG)#不阻塞，使用较少，除非子进程先退出，否则还是会产生僵尸进程
    signal(SIGCHLD,SIG_IGN)
    print "this is parent process",os.getpid()
    print pid
    while True:
        pass

print "+++++++++++++++++++++"


#僵尸进程：子进程先结束，父进程还存在，但是没有对子进程进行处理
#孤儿进程：父进程先退出，子进程还存在，孤儿进程是没有影响的，可以接受，会过给init，init会给孤儿进程收拾
#处理僵尸进程的三种办法： 1 os.wait()(这是个阻塞函数)返回一个元祖，元祖里面就是子进程的状态
#os.waitpid(pid,os.WNOHANG)功能和wait一样，比wait强大,pid==0,表示这个进程组任意一个子进程退出都会捕捉到pid==-1任何一个子进程退出都会捕捉到，pid>1pid为pid的进程退出，WNOHANG不阻塞,exit()直接退出
