#!/usr/bin/python3
"""
Este template serve de esqueleto para a criação de um filtro
que,no caso de ser fornecido o nome de um ficheiro como argumento,
itera sobre as suas linhas para as processar, ou então recebe essas linhas
a partir do standard input, caso não receba argumentos
"""

import fileinput

for line in fileinput.input():
	line = line.strip()
	print(fileinput.lineno(), line)
