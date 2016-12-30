#!/usr/bin/python

import os

print os.listdir('.')
print os.path.isdir('test')
print os.path.isfile('test')

file_path = os.path.join('home/linux','test','test.txt')
print file_path

filename = raw_input('file name:')

file_stat = os.stat(filename)

#os.system('ls -l')
