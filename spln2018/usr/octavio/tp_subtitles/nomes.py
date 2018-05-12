#!/usr/bin/python3.6

import fileinput, re, getopt, sys
import nltk

"""
CC   - conjuction (coordinating)
CD   - numeral (cardinal)
DT   - determiner
EX   - existential there
IN   - preposition/conjuction (subordinating)
JJ   - adjective/numeral (ordinal)
JJR  - adjective (comparative)
JJS  - adjective (superlative)
LS   - list item marker
MD   - modal auxiliary
NN   - noun (common and singular or mass)
NNP  - noun (proper and singular)
NNS  - noun (common and plural)
PDT  - pre-determiner (all, both, half, many, ...)
POS  - genetive marker ( 's )
PRP  - pronoun (personal)
PRP$ - pronoun (possessive)
RB   - adverb
RBR  - adverb (comparative)
RBS  - adverb (superlative)
RP   - particle (aside, before, over, behind, ...)
TO   - "to" as preposition or infinitive marker
UH   - interjection (huh, hush, anyways, wow, ...)
VB   - verb (base form)
VBD  - verb (past tense)
VBG  - verb (present participle or gerund)
VBN  - verb (past participle)
VBP  - verb (present tense, not 3rd person)
VBZ  - verb (present tense, 3rd person)
WDT  - WH-determiner (that, what, which, ...)
WP   - WH-pronoun (that, what, which, who, whom, ...)
WRB  - WH-adverb (how, where, why, ...)
"""
opcoes , args = getopt.getopt(sys.argv[1:],"dwn")

titles =[r"[Ss](?:enho)?r(?:a)?",
         r"[Mm]r(?:s)?(?:\.)?",
         r"[Mm]is(?:s|ter)"]
titles = "|".join(titles)



palMai = r"(?:\b[A-ZÀ-Ý]\w+|[A-ZÀ-Ý]\.)"
preposicao = r"d[eao]s?"
fimDeFrase = r"([^A-ZÀ-Ý][.!?]\s+|\n{2,}(?:-\s*)?)([A-ZÀ-Ý])"

nomeProprio= palMai + "(?: (?:"+preposicao+" )?"+palMai+")*"
#nomeProprio = f"({palMai}(?: (?:{preposicao} )?{palMai})*)"
palavra =r"(?:\b[A-Za-z]\w|*|[a-z]\.)" 

def namePP(dic):
    for key,val in sorted(dic.items(),key=lambda x: x[1] , reverse=True):
        print(key + " -> " + str(val))
        

def properNameBag(texto):
    nomes = {}
    texto = re.sub(fimDeFrase,r"\1_\2",texto)
    for nome in re.findall(nomeProprio,texto):
        tokens = nltk.tokenize.word_tokenize(nome)
        tag = nltk.pos_tag(tokens)[0]
        if tag[1] == 'NNP': 
            nomes[nome] = nomes.get(nome,0)+1
    return nomes

def wordBag(texto):
    # NNP, NN, VBZ, VBN,...
    filt =input()
    nomes = {}
    texto = re.sub(fimDeFrase,r"\1_\2",texto)
    for nome in re.findall(palavra,texto):
        tokens = nltk.tokenize.word_tokenize(nome)
        tag = nltk.pos_tag(tokens)[0]

        if tag[1] == filt: 
            nomes[nome] = nomes.get(nome,0)+1
    return nomes

def tagWord(text):
    word = text.group()
    token = nltk.tokenize.word_tokenize(word)
    tag = nltk.tag.pos_tag(token)[0]
    return "{"+str(tag[0])+", "+str(tag[1])+"}"

def properNameAnot(texto):
    texto = re.sub(fimDeFrase,r"\1_\2",texto)
    texto = re.sub(nomeProprio,r"{\1}",texto)
    texto = re.sub("_","",texto)
    return texto

def wordAnot(texto):
    texto = re.sub(fimDeFrase,r"\1_\2",texto)
    texto = re.sub(palavra,tagWord,texto)
    texto = re.sub("_","",texto)
    return texto

# ------------ MAIN -----------------

texto = "".join(fileinput.input(args))

if len(opcoes)>0 and opcoes[0][0] == '-d':
    namePP(properNameBag(texto))
elif len(opcoes)>0 and opcoes[0][0] == '-w':
    namePP(wordBag(texto))
elif len(opcoes)>0 and opcoes[0][0] == '-n':
    print(properNameAnot(texto))
else:
    print(wordAnot(texto))
