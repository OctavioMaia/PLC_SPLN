#!/usr/bin/python3
from nltk.tokenize import word_tokenize
from nltk import bigrams
import nltk
import collections
#nltk.download("punkt")
import sys

a = sys.argv
if len(a) > 1 :
  f = open(a[1], "r").read()
else:
  exit(1)

lista_palavras = word_tokenize(f)

print(collections.Counter(list(bigrams(lista_palavras))))