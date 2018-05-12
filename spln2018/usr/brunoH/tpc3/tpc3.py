#!/usr/bin/python3
"""
Script para identificar nomes próprios no Harry Potter
"""

import fileinput,re,operator
from pprint import pprint

dic={}
texto = "".join(fileinput.input())
janela =re.findall(r"(\{[\w+\s\w+]+\})+(?=(.{1,66}))",texto)

for interacao in janela:
    key=interacao[0]
    key=key.replace("{","")
    key=key.replace("}","")
    Lval=re.findall(r"(\{[\w+\s\w+]+\})+",interacao[1])

    if key in dic:
        if len(Lval)>0:
            for value in Lval:
                value=value.replace("{","")
                value=value.replace("}","")
                if value in dic[key]:
                    dic[key][value]=dic[key][value]+1
                else:
                    dic[key][value]=1
    
    else:
        dic[key]={}
        if len(Lval)>0:
            for value in Lval:
                value=value.replace("{","")
                value=value.replace("}","")
                if value in dic[key]:
                    dic[key][value]=dic[key][value]+1
                else:   
                    dic[key][value]=1


print("""
    <html>
    <head>
        <meta charset="UTF8"/>
        <title>Interação de Personagens</title>
        <script>
        $(window).on("load resize ", function(){
            var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
         $('.tbl-header').css({'padding-right':scrollWidth});
        })
        </script>
        <style>
                        h1{
            font-size: 30px;
            color: #fff;
            text-transform: uppercase;
            font-weight: 300;
            text-align: center;
            margin-bottom: 15px;
            }
            table{
            width:100%;
            
            }
            .tbl-header{
            background-color: rgba(255,255,255,0.3);
            }
            .tbl-content{
            height:300px;
            overflow-x:auto;
            margin-top: 0px;
            border: 1px solid rgba(255,255,255,0.3);
            }
            th{
            padding: 20px 15px;
            text-align: left;
            font-weight: 500;
            font-size: 12px;
            color: #fff;
            text-transform: uppercase;
            }
            td{
            padding: 15px;
            text-align: left;
            vertical-align:middle;
            font-weight: 300;
            font-size: 12px;
            color: #fff;
            border-bottom: solid 1px rgba(255,255,255,0.1);
            }


            /* demo styles */

            @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
            body{
            background: -webkit-linear-gradient(left, #25c481, #25b7c4);
            background: linear-gradient(to right, #25c481, #25b7c4);
            font-family: 'Roboto', sans-serif;
            }
            section{
            margin: 50px;
            }
            /* for custom scrollbar for webkit browser*/

            ::-webkit-scrollbar {
                width: 6px;
            } 
            ::-webkit-scrollbar-track {
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
            } 
            ::-webkit-scrollbar-thumb {
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
            }
        </style>
    </head>
    <body>
        <section>
            <h1> Interação de Personagens do Harry poter</h1>
            <div class="tbl-header">
            <table cellpadding="0" cellspacing="0" border="0">
            <thead>
            <tr>
                <th>Personagem</th> 
                <th >interações</th>
            </tr>
            </thead>
            </table>
            </div>
            <div class="tbl-content">
                <table cellpadding="0" cellspacing="0" border="0">
                <tbody>
""")

i=0
max=0
total=0
personagem=""
for entry in dic: 
    i=0
    if dic[entry]!={}:
        print("<tr>\n<td> %s </td>" % (entry))
        for value in dic[entry]:
            i=i+1
            total=total+dic[entry][value]       
            print("<td>%s:%d</td>" % (value , dic[entry][value]))
        if i>max:
            max=i
            personagem=entry            
        print("</tr>")

print("</tbody></table></div></section>")
print("<section> <h5> Personagem com mais interaçoes: %s</h5>" %(personagem))
print("<h5> Numero de interaçoes com %s: %d</h5>" %(personagem,max))
print("<h5> Número total de interações: %d</h5></section>"%(total))
print("</body> </html>") 


