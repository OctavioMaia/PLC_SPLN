#!/usr/bin/python3
import fileinput


dic = {}
dic2 = {}
def f_net(dic):
	res = 0
	for tuplo in dic.items():
		res=res + tuplo[1]
	for outro in dic:
		substi[0] = outro[0]
		substi[1] = outro[1] * 1000000/ res
		dic2[substi] = outro 
	return res

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
