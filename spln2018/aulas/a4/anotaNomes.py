#!/usr/bin/python3.6
import fileinput, re, getopt, sys

opcoes , args = getopt.getopt(sys.argv[1:],"d")

titles =[r"[Ss](?:enho)?r(?:a)?",
         r"[Mm]r(?:s)?(?:\.)?",
         r"[Mm]is(?:s|ter)"]
titles = "|".join(titles)

palMai = r"(?:\b[A-ZÀ-Ý]\w+|[A-ZÀ-Ý]\.)"
preposicao = r"d[eao]s?"
fimDeFrase = r"([^A-ZÀ-Ý][.!?]\s+|\n{2,}(?:-\s*)?)([A-ZÀ-Ý])"

#nomeProprio= palMai + "(?: (?:"+preposicao+" )?"+palMai+")*"
nomeProprio = f"({palMai}(?: (?:{preposicao} )?{palMai})*)"

def namePP(dic):
    for key,val in sorted(dic.items(),key=lambda x: x[1] , reverse=True):
        print(key + " -> " + str(val))
        
def properNameBag(texto):
    nomes = {}
    texto = re.sub(fimDeFrase,r"\1_\2",texto)
    for nome in re.findall(nomeProprio,texto):
        nomes[nome] = nomes.get(nome,0)+1
    return nomes

def properNameAnot(texto):
    texto = re.sub(fimDeFrase,r"\1_\2",texto)
    texto = re.sub(nomeProprio,r"{\1}",texto)
    texto = re.sub("_","",texto)
    return texto

# ------------ MAIN -----------------

texto = "".join(fileinput.input(args))

if len(opcoes)>0 and opcoes[0][0] == '-d':
    namePP(properNameBag(texto))
else:
    print(properNameAnot(texto))

