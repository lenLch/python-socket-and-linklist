#!/usr/bin/python
# coding=utf-8

import sys

f = open(sys.argv[1],'r')
f_cp = open(sys.argv[2],'w')

while True:
    str = f.readline(10)
    if str == '':
        break
    f_cp.write(str)

f.close()
f_cp.close()
