#!/usr/bin/python3


import fileinput, re


regex = r'[A-Z]\w+(?:\s(?:da|de)\s[A-Z]\w+)?'

dic = []

for line in fileinput.input():
    line = line.strip()
    for token in re.findall(regex, line):
        line = line.replace(token, "{"+token+"}")
    print (line) 
