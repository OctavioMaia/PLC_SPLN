#!/usr/bin/python3
"""
bloco de comentários
spln2018
"""

import fileinput

#print hello world
msg = 'Hello world!'
print(msg)

#read from file
"""
i=0
for line in open('exemplo.txt').readlines():
    i=i+1
    line = line.strip()
    print(i,line)


for line in fileinput.input():
    line = line.strip()
    print(fileinput.lineno(), line)
"""

for line in fileinput.input():
    print(line.replace('repetidas',''))