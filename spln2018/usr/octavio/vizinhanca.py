#!/usr/bin/python3
import fileinput, re, pprint, getopt, sys

texto = ''.join(fileinput.input())
#print(texto)


def vizinhanca(texto):
	dic={}
	exp = r"{(.+?)}(?=((?:.|\n){1,100}))"
	for nome in re.findall(exp,texto):
		for nome2 in re.findall(r"{(.+?)}",nome[1]):
			if nome[0] not in dic:
				dic[nome[0]] = {nome2 : 1}
			else:
				dic[nome[0]][nome2] = dic[nome[0]].get(nome2,0)+1
			if nome2 not in dic:
				dic[nome2] = {nome[0] : 1}
			else:
				dic[nome2][nome[0]] = dic[nome2].get(nome[0],0)+1
	return dic			
	

pprint.pprint(vizinhanca(texto))