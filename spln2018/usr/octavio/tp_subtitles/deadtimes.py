#!/usr/bin/python3
import fileinput, re

numSub = r"^([0-9])+(?!.)"   #expressão regular para o número da legenda no formato srt
time = r"([0-9]+[:])+[0-9]+[,][0-9]+" #exp regular para o tempo da legenda no formato srt 
text = r'[A-Za-z]' 					  #exp. regular para o texto da legenda no formato srt
threshold = 15 						  #threshold para deadtime

def anot(subtitles): #função que anota o ficheiro com identificação do número 
					 #da linha, e o "tipo" da mesma, isto é, se é número de legenda,
					 #texto ou o tempo.
	lastSentence=currentSentence=string=[]
	lastSecond=lastMinute=lastHour=0
	currentSecond=currentMinute=currentHour=0
	deadTimeHour=deadTimeMinute=deadTimeSeconds=0

	i=0 										#int para escrever no ficheiro o número da linha em causa
	fileAnot = open("legendaAnotadas.txt", "w") #abre o ficheiro para onde vamos "anotar" o programa
	for line in subtitles: 						#percorre todas as linhas do ficheiro
		if(re.findall(time, line) != []): 		#se encontrar uma linha com tempo escreve:
			line = str(i)+ " Time ------> " + line
			string = line.split('--> ')
			currentSentence = string[1].split(':')
			currentHour = currentSentence[0]
			currentMinute = currentSentence[1]
			currentSecond = currentSentence[2].split(',')[0]

			if(lastSecond!=0 or lastMinute!=0 or lastHour!=0):
				diffHour   = int(currentHour)   - int(lastHour)
				if(int(currentSecond) < int(lastSecond)):
					diffMinute = int(currentMinute) - int(lastMinute)-1
					diffSecond = 60 - int(lastSecond) + int(currentSecond)
					if(diffHour > 0):
						deadTimeHour += diffHour
					if(diffMinute > 0):
						deadTimeMinute += diffMinute
					if(diffSecond > threshold):
						if(deadTimeSeconds+diffSecond>=60):
							deadTimeMinute+=1
							deadTimeSeconds=diffSecond+deadTimeSeconds-60
						else:
							deadTimeSeconds += diffSecond	
				else:
					diffMinute = int(currentMinute) - int(lastMinute)
					diffSecond = int(currentSecond) - int(lastSecond)
					if(diffHour > 0):
						deadTimeHour += diffHour
					if(diffMinute > 0):
						deadTimeMinute += diffMinute
					if(diffSecond > threshold):
						if(deadTimeSeconds+diffSecond>=60):
							deadTimeMinute+=1
							deadTimeSeconds=diffSecond+deadTimeSeconds-60
						else:
							deadTimeSeconds += diffSecond				
				print("Time difference -> " + str(diffHour)+':'+str(diffMinute)+':'+str(diffSecond))	
			lastSentence = string[2].split(':')
			lastHour = lastSentence[0]
			lastMinute = lastSentence[1]
			lastSecond = lastSentence[2].split(',')[0]
		elif(re.findall(text, line) != []): #se encontrar uma linha com texto escreve:
				line = str(i) + " Text ------> " + line	
		elif(re.findall(numSub, line) != []): #se encontrar uma linha com o número da legenda escreve:
				line = str(i) + " NumS ------> " + line
		else:  #se a linha for apenas um "\n", escreve:
			line = str(i) + line
		fileAnot.write(line) #escreve a linha no ficheiro
		i+=1 #incrementa o número da linha
	print("Total dead time -> " + str(deadTimeHour) + ':'+ str(deadTimeMinute) + ':' + str(deadTimeSeconds))
	fileAnot.close() #para fechar o ficheiro

#_____Main______
subtitles = fileinput.input()  #ler o input
anot(subtitles)