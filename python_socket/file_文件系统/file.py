#!/usr/bin/python
# coding=utf-8

import sys

f = open(sys.argv[1],'w+')

while True:
    str = sys.stdin.readline()
    if str == '#\n':
        break
    f.write(str)

f.close()
