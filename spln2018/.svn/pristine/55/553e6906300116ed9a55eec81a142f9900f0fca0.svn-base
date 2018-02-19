import fileinput

dic = {}

for line in fileinput.input():
	line = line.strip()
	dic[line]=dic.get(line,0)+1
	if(dic[line] <= 1):
		print(line)
