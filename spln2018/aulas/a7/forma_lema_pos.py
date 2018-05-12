#!/usr/bin/python3
for line in open("texto2_tagged.txt","r").readlines():
	

	tokens = line.split()
	if len(tokens) > 2:
		print(tokens[0] + "=" + tokens[1] + "+" + tokens[2] ,end=" ")
	else:
		print()