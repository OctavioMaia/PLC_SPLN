#!/usr/bin/python3
"""
Script para extrair um dicionário de um corpora CETEM público
"""

import fileinput
import re
from pprint import pprint
import shelve

dic = shelve.open("dicionario_publico",writeback=True)

for line in fileinput.input():
    #if fileinput.filelineno() > 100:
    #    break
    line = line.strip()
    toks = re.split("\s",line)
    if len(toks) > 5:
        word = toks[0]
        lema = toks[3]
        pos = toks[4]
        if word not in dic:
                dic[word] = {(lema,pos) : 1}
        else:
            dic[word][(lema,pos)] = dic[word].get((lema,pos),0) + 1
            
#pprint(dic)
