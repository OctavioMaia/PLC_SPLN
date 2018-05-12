#!/usr/bin/python3
"""
script para tokenizar e normalizar linhas e tokens
"""

import re
import fileinput


def f_rel(dic):
	res = sum(dic.values())
	return  { word : val*(1000000/res) for word, val in dic.items()}

def pretty_print(dic):
	for word , val in sorted(dic.items(), key = lambda x : x[1], reverse = True):
		print(str(val) + ' -> ' + word)	


lista= [r'\w+(?:-\w+)*',
		r'[.,!?-]+',
		r'\d+\.\d+']
tokensExp = "|".join(lista)
dic = {}

for line in fileinput.input():
	line = line.strip()
	for token in re.findall(tokensExp, line):
		dic[token]=dic.get(token,0)+1

if '' in dic:
	del dic[''] 

pretty_print(f_rel(dic))
