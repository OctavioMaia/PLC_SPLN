#!/usr/bin/python3
import fileinput


def f_rel(dic):
	
	res = sum(dic.values())
	
	return  { word : val*(1000000/res) for word, val in dic.items()}

def pretty_print(dic):
	
	for word , val in sorted(dic.items(), key = lambda x : x[1], reverse = True):
		print(str(val) + ' -> ' + word)	


dic = {}

for line in fileinput.input():
	line = line.strip()
	line = line.replace('.', ' .')
	line = line.replace(',', ' ,')
	for word in line.split(' '):
		dic[word]=dic.get(word,0)+1

if '' in dic:
	del dic[''] 

pretty_print(f_rel(dic))



 