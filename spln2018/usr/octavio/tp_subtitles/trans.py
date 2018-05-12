#!/usr/bin/python3.6
import fileinput, sys
import sync as f

sub1 = fileinput.input(sys.argv[1])
sub2 = fileinput.input(sys.argv[2])
dic1= f.createDicTextTime(sub1)
dic2= f.createDicTextTime(sub2)

set1 = set(dic1)
set2 = set(dic2)


for n in set1.intersection(set2):
	line = n + "\n" 
	for i in dic1[n]:
		line = line + "".join(str(i).replace("\n", " "))
	line = line + "---> " 
	for i in dic2[n]:
		line = line + "".join(str(i).replace("\n", " "))
	line = line + "\n"
	line.replace(" ", "")
	print(line)

