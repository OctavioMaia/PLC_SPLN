#!/usr/bin/python3
"""
 template for filters
"""
import re,sys, getopt, fileinput, pprint
'''
try: 
    _op, A =getopt.getopt(sys.argv[1:],"a:e")
    opt=dict(_op)
except getopt.GetoptError as err:
    print(str(err))
#    usage()
    sys.exit(2)
'''
text = ''.join(fileinput.input())


def vizinhanca(text,jan = 100):
    dic = {}
    oco = {}
    pattern = r"{(.+?)}(?=((?:.|\n){1," + str(jan) + "}))"
    for nome,ctx in re.findall(pattern,text):

        oco[nome] = oco.get(nome,0) + 1

        for nome2 in re.findall(r"{(.+?)}",ctx):    
            if nome in dic:
                dic[nome][nome2] =  dic[nome].get(nome2,0) + 1
            else:
               dic[nome]= {nome2 : 1}
            if nome2 in dic:
                dic[nome2][nome] =  dic[nome2].get(nome,0)+ 1
            else:
               dic[nome2]= {nome : 1} 

    return dic,oco

def viz_filter(dic,max = 10):

    dic_new = {} 
    for pal,dic_p in dic.items():
        dic_new[pal] = dict(sorted(dic_p.items(), 
                                    key = lambda x : x[1], 
                                    reverse  = True)[0:max])
    
    return dic_new

def viz_to_site(dic):
    for pal,dic_pal in dic.items():
        fd = open('html/'+pal+'.html','w')
        p = ''.join([f'<li><a href="{x}.html">{x}</a></li>' for x in dic_pal.keys()])
        fd.write(f'''<html><body><h1>{pal}</h1>
                    <ol>{p}</ol>
                    </body></html>''')
        fd.close()

(dic,oco) = vizinhanca(text,120)
viz_to_site(viz_filter(dic))
#pprint.pprint(viz_filter(dic))
#pprint.pprint(oco)