


import fileinput
dic = {}

for line in fileinput.input():
	line = line.strip()
	if line not in dic:
		dic[line] = 1	
		print(line);
