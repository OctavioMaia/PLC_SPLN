#!/usr/bin/python3
"""
Script para consultar palavras num dicionário de um corpora CETEM público
"""

import fileinput
import re
from pprint import pprint
import shelve
import os

home_dir = os.environ["HOME"]
#print(home_dir)
dic = shelve.open(home_dir + "/dicts/dicionario_publico",writeback=True)

for line in fileinput.input():
    line=line.strip()
    
    pprint(dic.get(line,"Desconhecido"))
