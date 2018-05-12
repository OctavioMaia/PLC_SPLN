import itertools
import re
teclado = { "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
    }


def palavra_para_numeros(palavra):
    res = ""
    for letra in palavra:
        for numero in teclado:
            if letra in teclado[numero]:
                res+=numero
                break
    return res

def grep_palavra(regex):
    res = []
    f = open("formasMeioMilhao.txt","r", encoding="utf-8")
    for line in f.readlines():
        palavra = line.split("\t")[1].strip()
        
        if re.fullmatch(regex, palavra, flags=re.I):
            res.append(palavra)
    return res

def numeros_para_expReg(numeros):
    res = r""
    for numero in numeros:
        res += r"["
        for letra in teclado[numero]:
            res += letra
        res += r"]"
    return res

inp=""
while inp != "quit":
    inp = input(">>")
    print(grep_palavra(numeros_para_expReg(palavra_para_numeros(inp))))
