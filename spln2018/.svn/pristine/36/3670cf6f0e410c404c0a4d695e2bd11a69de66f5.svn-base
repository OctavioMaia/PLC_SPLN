#!/usr/bin/python3
import re
import random

def resp(inp):
    for (patt,resps) in regras:
        r = re.findall(patt,inp)
        if r :
            res = random.choice(resps)
            if callable(res) :
                return res(r[0])
            else:
                return res
    return "Não entendi"


inp = ""
favoritos = {"músico": "Zé Cabra",
             "futebolista":"Cristiano Ronaldo"
            }
regras = [(r"chamas",["Diz tu primeiro","Chamo-me Itelvina"]),
          (r"(\w+) favorito",[ lambda x : "O " + favoritos.get(x,x+"... não sei")])
         ]
while(inp!="xau"):
    inp=input(">>")
    print(resp(inp))


