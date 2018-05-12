#!/usr/bin/python3.6
import fileinput
import re

toksExpr = [
        r"\w+(?:-\w+)*",
        r"\d+\.\d+",
        r"[.?!,-]+"]
toksExpr = "|".join(toksExpr)
toks = []
texto = "".join(fileinput.input())
paragrafos = re.split(r"(?:\n\n)+",texto)
for paragrafo in paragrafos:
    toks.append(re.findall(toksExpr,paragrafo))


for paragrafo in toks:
        print(" ".join(paragrafo))+"\n")
