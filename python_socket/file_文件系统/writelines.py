#!/usr/bin/env python
# coding=utf-8

f = open("test.txt",'w')

l = ['nihao\n','hi\n','hello\n','how are you\n','how do you do\n']

f.writelines(l)
