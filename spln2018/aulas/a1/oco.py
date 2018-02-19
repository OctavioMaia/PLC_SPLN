#!/usr/bin/python3
import fileinput


dic = {}

for line in fileinput.input():
	line = line.strip()
	line = line.replace('.', ' .')
	line = line.replace(',', ' ,')
	for word in line.split(' '):
		dic[word]=dic.get(word,0)+1

if '' in dic:
	del dic[''] 
	

for word , val in sorted(dic.items(),key= lambda x : x[1], reverse = True):
	print(val , word)
