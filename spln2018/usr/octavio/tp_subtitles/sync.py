#!/usr/bin/python3
import fileinput, re, collections

numSub = r"^([0-9])+(?!.)"   #expressão regular para o número da legenda no formato srt
time = r"([0-9]+[:])+[0-9]+[,][0-9]+" #exp regular para o tempo da legenda no formato srt 
text = r"[0-9]*['\s']?[A-Za-z]+" #exp. regular para o texto da legenda no formato srt


def createDicTextTime(subtitles): #cria um dicionário com o número da legenda e o texto da mesma
	listText = [] #lista com todas as ocorrências de frases 
	numText=0 #indica o número 
	dicTime = {} #dicionario com {numero da legenda: tempo da legenda}
	numTime=1 #indica o número do tempo

	for line in subtitles:
		if(re.findall(time, line) != []):
			dicTime.update({numTime : line[0:8]})
			numTime += 1
		elif(re.findall(text, line) != []):
				listText.append(line)
				numText +=1
		elif(re.findall(numSub,line) !=[]):
			pass
		else: 
			listText.append(line) 
			numText +=1

	j = 0
	eachSub = {}
	sub = 1	

	for sentence in listText:
		if j < numText-1:
			z=0
			string = []
			if listText[j] != "\n":
				while listText[j+z] != "\n":
					string.append(listText[j+z])
					z += 1
				eachSub.update({sub : string})
				sub += 1
			j = j+z+1

	
	
	finalDic = {}

	for keyText,keyTime in zip(eachSub,dicTime):
		finalDic.update({dicTime.get(keyTime) : eachSub.get(keyText)})
	od = collections.OrderedDict(sorted(finalDic.items()))
	return od


#_____Main______
subtitles = fileinput.input()  #ler o input
createDicTextTime(subtitles)








		


















	


